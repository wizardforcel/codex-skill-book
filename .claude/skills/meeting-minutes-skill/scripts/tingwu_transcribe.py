#!/usr/bin/env python3
import argparse
import json
import mimetypes
import os
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen

import oss2
from alibabacloud_tea_openapi.models import Config
from alibabacloud_tingwu20230930.client import Client as TingwuClient
from alibabacloud_tingwu20230930 import models as tingwu_models
from dotenv import load_dotenv


ROOT = Path.cwd()
OUTPUTS = ROOT / "outputs"
ENV_FILE = Path.home() / ".codex" / "meeting-minutes.env"


def die(message: str) -> None:
    print(f"错误：{message}", file=sys.stderr)
    raise SystemExit(1)


def getenv_required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        die(f"缺少环境变量 {name}。请参考 work/.env.example 创建 work/.env。")
    return value


def timestamp_ms(ms) -> str:
    if ms is None:
        return ""
    try:
        total = int(ms) / 1000
    except (TypeError, ValueError):
        return ""
    minutes = int(total // 60)
    seconds = int(total % 60)
    return f"{minutes:02d}:{seconds:02d}"


def create_oss_bucket():
    access_key_id = getenv_required("ALIBABA_CLOUD_ACCESS_KEY_ID")
    access_key_secret = getenv_required("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
    endpoint = getenv_required("OSS_ENDPOINT")
    bucket_name = getenv_required("OSS_BUCKET")
    auth = oss2.Auth(access_key_id, access_key_secret)
    return oss2.Bucket(auth, f"https://{endpoint}", bucket_name)


def create_tingwu_client():
    access_key_id = getenv_required("ALIBABA_CLOUD_ACCESS_KEY_ID")
    access_key_secret = getenv_required("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
    region = getenv_required("OSS_REGION")
    endpoint = os.getenv("TINGWU_ENDPOINT") or f"tingwu.{region}.aliyuncs.com"
    config = Config(
        access_key_id=access_key_id,
        access_key_secret=access_key_secret,
        region_id=region,
        endpoint=endpoint,
    )
    return TingwuClient(config)


def upload_audio(audio_path: Path, keep_days: int) -> tuple[str, str]:
    bucket = create_oss_bucket()
    suffix = audio_path.suffix.lower() or ".m4a"
    object_key = f"meeting-audio/{datetime.now().strftime('%Y%m%d')}/{uuid.uuid4().hex}{suffix}"
    content_type = mimetypes.guess_type(audio_path.name)[0] or "application/octet-stream"

    print(f"上传音频到 OSS：{object_key}")
    with audio_path.open("rb") as f:
        bucket.put_object(object_key, f, headers={"Content-Type": content_type})

    signed_url = bucket.sign_url("GET", object_key, keep_days * 24 * 3600)
    return object_key, signed_url


def submit_tingwu_task(file_url: str, speaker_count: int, task_key: str):
    client = create_tingwu_client()
    request = tingwu_models.CreateTaskRequest(
        type="offline",
        app_key=getenv_required("TINGWU_APPKEY"),
        input=tingwu_models.CreateTaskRequestInput(
            source_language="cn",
            file_url=file_url,
            task_key=task_key,
            progressive_callbacks_enabled=False,
        ),
        parameters=tingwu_models.CreateTaskRequestParameters(
            transcription=tingwu_models.CreateTaskRequestParametersTranscription(
                diarization_enabled=True,
                diarization=tingwu_models.CreateTaskRequestParametersTranscriptionDiarization(
                    speaker_count=speaker_count,
                ),
                output_level=1,
            ),
            summarization_enabled=False,
            meeting_assistance_enabled=False,
            auto_chapters_enabled=False,
            text_polish_enabled=False,
        ),
    )
    response = client.create_task(request)
    body = response.body
    if str(body.code) != "0":
        die(f"CreateTask 失败：{body.code} {body.message}")
    task_id = body.data.task_id
    if not task_id:
        die(f"CreateTask 未返回 TaskId：{body.to_map()}")
    print(f"听悟任务已提交：{task_id}")
    return task_id, body.to_map()


def wait_for_task(task_id: str, poll_seconds: int, timeout_minutes: int):
    client = create_tingwu_client()
    deadline = time.time() + timeout_minutes * 60
    last_status = None
    transient_errors = 0
    while time.time() < deadline:
        try:
            response = client.get_task_info(task_id)
        except Exception as exc:
            transient_errors += 1
            if transient_errors > 10:
                raise
            print(f"查询任务状态暂时失败，稍后重试：{exc}")
            time.sleep(poll_seconds)
            continue
        transient_errors = 0
        body = response.body
        if str(body.code) != "0":
            die(f"GetTaskInfo 失败：{body.code} {body.message}")
        data = body.data
        status = data.task_status
        if status != last_status:
            print(f"任务状态：{status}")
            last_status = status
        if status == "COMPLETED":
            return body.to_map()
        if status in {"FAILED", "INVALID"}:
            die(f"听悟任务失败：{data.error_code} {data.error_message}")
        time.sleep(poll_seconds)
    die(f"等待超时：{timeout_minutes} 分钟内未完成。可以稍后用 TaskId 查询：{task_id}")


def fetch_json(url: str):
    with urlopen(url, timeout=60) as response:
        raw = response.read()
    return json.loads(raw.decode("utf-8"))


def find_segments(data):
    if isinstance(data, dict):
        for key in ("Sentences", "sentences", "Paragraphs", "paragraphs"):
            value = data.get(key)
            if isinstance(value, list):
                return value
        for value in data.values():
            found = find_segments(value)
            if found:
                return found
    if isinstance(data, list):
        for item in data:
            found = find_segments(item)
            if found:
                return found
    return []


def speaker_of(segment):
    for key in ("SpeakerId", "Speaker", "speaker_id", "speaker", "ChannelId", "channel_id"):
        if key in segment and segment[key] not in (None, ""):
            return f"说话人{segment[key]}"
    return "说话人?"


def text_of(segment):
    for key in ("Text", "text", "Sentence", "sentence"):
        value = segment.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    words = segment.get("Words") or segment.get("words")
    if isinstance(words, list):
        parts = []
        for word in words:
            if isinstance(word, dict):
                parts.append(str(word.get("Text") or word.get("text") or ""))
            else:
                parts.append(str(word))
        return "".join(parts).strip()
    return ""


def start_time_of(segment):
    for key in ("BeginTime", "StartTime", "begin_time", "start_time", "Begin", "begin"):
        if key in segment:
            return segment[key]
    words = segment.get("Words") or segment.get("words")
    if isinstance(words, list) and words:
        first = words[0]
        if isinstance(first, dict):
            for key in ("Start", "start", "BeginTime", "begin_time"):
                if key in first:
                    return first[key]
    return None


def write_transcript_markdown(path: Path, transcription_json, task_id: str, source_name: str):
    segments = find_segments(transcription_json)
    lines = [
        f"# 原始转写稿",
        "",
        f"- 音频文件：{source_name}",
        f"- 听悟 TaskId：{task_id}",
        f"- 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]
    if not segments:
        lines.extend([
            "> 未能自动识别转写 JSON 的句子结构。请查看同目录 raw-transcription JSON。",
            "",
        ])
    for segment in segments:
        if not isinstance(segment, dict):
            continue
        text = text_of(segment)
        if not text:
            continue
        stamp = timestamp_ms(start_time_of(segment))
        prefix = f"[{stamp}] " if stamp else ""
        lines.append(f"{prefix}**{speaker_of(segment)}**：{text}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="上传音频到 OSS 并调用通义听悟离线转写。")
    parser.add_argument("audio", help="本地音频文件路径，例如 /path/to/meeting.m4a")
    parser.add_argument("--speaker-count", type=int, default=0, help="说话人数。0 表示不确定，由通义听悟自动判断。")
    parser.add_argument("--poll-seconds", type=int, default=20, help="轮询间隔秒数。")
    parser.add_argument("--timeout-minutes", type=int, default=180, help="最长等待分钟数。")
    parser.add_argument("--signed-url-days", type=int, default=1, help="OSS 临时下载链接有效天数。")
    parser.add_argument("--keep-oss", action="store_true", help="转写完成后保留 OSS 上的临时音频。")
    args = parser.parse_args()

    load_dotenv(ENV_FILE)
    audio_path = Path(args.audio).expanduser().resolve()
    if not audio_path.exists():
        die(f"找不到音频文件：{audio_path}")
    if not audio_path.is_file():
        die(f"不是文件：{audio_path}")

    OUTPUTS.mkdir(exist_ok=True)
    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
    task_key = f"meeting-transcribe-{run_id}"
    result_dir = OUTPUTS / task_key
    result_dir.mkdir(parents=True, exist_ok=True)

    object_key = None
    task_submitted = False
    task_completed = False
    try:
        object_key, signed_url = upload_audio(audio_path, args.signed_url_days)
        task_id, create_response = submit_tingwu_task(signed_url, args.speaker_count, task_key)
        task_submitted = True
        task_info = wait_for_task(task_id, args.poll_seconds, args.timeout_minutes)
        task_completed = True

        (result_dir / "create-task-response.json").write_text(
            json.dumps(create_response, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (result_dir / "task-info.json").write_text(
            json.dumps(task_info, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        result = (((task_info.get("Data") or {}).get("Result")) or {})
        transcription_url = result.get("Transcription")
        if not transcription_url:
            die("任务完成，但没有返回 Transcription 结果链接。")
        transcription_json = fetch_json(transcription_url)
        (result_dir / "raw-transcription.json").write_text(
            json.dumps(transcription_json, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        write_transcript_markdown(result_dir / "transcript.md", transcription_json, task_id, audio_path.name)

        print("")
        print("完成。结果已保存：")
        print(result_dir)
        print(result_dir / "transcript.md")
    finally:
        if object_key and not args.keep_oss and (task_completed or not task_submitted):
            try:
                create_oss_bucket().delete_object(object_key)
                print(f"已删除 OSS 临时音频：{object_key}")
            except Exception as exc:
                print(f"提示：OSS 临时音频删除失败，需要手动检查：{object_key}；原因：{exc}", file=sys.stderr)
        elif object_key and task_submitted and not task_completed:
            print(f"任务尚未完成，已保留 OSS 临时音频：{object_key}")


if __name__ == "__main__":
    main()

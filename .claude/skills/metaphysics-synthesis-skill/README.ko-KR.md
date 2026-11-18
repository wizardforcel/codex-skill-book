# 형이상학 종합 스킬

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab)](scripts/)


형이상학 종합 스킬은 인공지능 에이전트가 사주팔자, 매화역수, 육효, 풍수 방향 분석, 타로 리딩을 구조적으로 다루도록 돕는 재사용 가능한 스킬 패키지입니다. 이 저장소는 단순한 점술 프롬프트가 아닙니다. 질문을 먼저 분류하고, 필요한 입력을 확인하고, 적합한 체계를 선택하고, 결론과 근거, 시기, 행동, 검증 신호를 분리하여 답하도록 설계된 절차입니다. Codex, Claude Code, 그리고 로컬 파일을 읽을 수 있는 다른 인공지능 에이전트 환경에서 사용할 수 있습니다.

일반적인 인공지능 점술 답변은 쉽게 흐려집니다. 사주와 타로와 풍수를 한 문장 안에 섞고, 하나의 상징을 너무 크게 해석하며, 사용자가 듣고 싶은 말로 마무리하는 경우가 많습니다. 이 스킬은 그런 방식을 피합니다. 사주는 인생 구조와 대운, 세운, 직업과 재물 흐름을 봅니다. 매화역수는 시간, 숫자, 외응, 갑작스러운 사건의 움직임을 봅니다. 육효는 계약, 승진, 상사, 급여, 프로젝트 성패처럼 구체적인 결과를 봅니다. 풍수는 좌석, 방향, 문, 창문, 동선, 소음, 시야, 지지 구조를 봅니다. 타로는 관계의 역학, 심리적 압력, 선택의 갈림길, 상징적 전환점을 봅니다.

이 스킬은 단호한 결론을 지향하지만 무리한 확정을 하지 않습니다. 입력이 부족하면 `runnable`, `partial`, `blocked` 중 하나로 상태를 나눕니다. 출생 시간이 불확실하면 시주와 관련된 세부 판단을 강하게 말하지 않습니다. 육효의 여섯 줄 순서가 불명확하면 납갑 세부 판단을 제한합니다. 풍수에서 나침반 방위와 평면도가 없으면 현공비성 같은 정밀 공식 판단을 하지 않습니다. 타로에서 사용자가 이미 카드를 제공했다면 다시 뽑지 않고, 도구가 카드를 뽑아야 할 때는 시드를 남겨 재현 가능하게 만듭니다.

## 언어

- [영어](README.md)
- [중국어 간체](README.zh-CN.md)
- [한국어](README.ko-KR.md)
- [일본어](README.ja-JP.md)
- [프랑스어](README.fr-FR.md)
- [스페인어](README.es-ES.md)

## 누구에게 적합한가

이 저장소는 인공지능 에이전트에게 동아시아 명리와 서양 타로를 안정적으로 다루게 하고 싶은 사용자에게 적합합니다. 매번 긴 프롬프트를 새로 작성하지 않고, 스킬 폴더를 설치한 뒤 에이전트가 `SKILL.md`와 필요한 `references/` 파일을 읽도록 만들 수 있습니다. 또한 사주, 매화역수, 육효, 풍수, 타로를 포함한 상담형 제품이나 자동화 도구를 만들 때도 유용합니다. 입력 계약, 출력 템플릿, 계산 보조 스크립트, 개인정보 점검 스크립트가 함께 제공되기 때문에 공개 저장소나 내부 도구로 확장하기 쉽습니다.

## 지원 체계

| 체계 | 약 100자 소개 | 주요 파일 |
| --- | --- | --- |
| [사주팔자](https://ko.wikipedia.org/wiki/%EC%82%AC%EC%A3%BC%ED%8C%94%EC%9E%90) | 사주는 태어난 연월일시를 네 기둥으로 보고, 천간과 지지의 관계로 성향, 직업, 재물, 관계, 건강 경향, 대운과 세운을 해석합니다. 이 스킬은 계산 가능한 명식 정보와 해석을 분리해 불확실한 입력을 과장하지 않습니다. | `references/bazi.md` |
| [매화역수 / 주역](https://ko.wikipedia.org/wiki/%EC%A3%BC%EC%97%AD) | 매화역수는 시간, 숫자, 방향, 소리, 물건, 외부 징조를 통해 가까운 사건의 움직임을 읽는 방식입니다. 본괘, 동효, 호괘, 변괘, 체용 관계, 외응을 각각의 근거로 분리해 판단합니다. | `references/meihua.md` |
| [육효 / 납갑](https://en.wikipedia.org/wiki/Wenwanggua) | 육효는 여섯 줄의 음양과 동변을 통해 구체적인 성패, 상대, 문서, 돈, 경쟁자, 시기와 장애물을 봅니다. 이 스킬은 초효부터 상효까지의 순서를 고정하고, 납갑 정보가 부족하면 부분 판단으로 표시합니다. | `references/liuyao.md` |
| [풍수](https://ko.wikipedia.org/wiki/%ED%92%8D%EC%88%98) | 풍수는 공간의 방향, 지지 구조, 문과 창, 동선, 소음, 시야, 압박선을 읽습니다. 이 스킬은 형세를 먼저 보고 방향 상징은 그 다음에 적용합니다. 비싼 처방보다 실제 환경 개선을 우선합니다. | `references/fengshui.md` |
| [타로](https://ko.wikipedia.org/wiki/%ED%83%80%EB%A1%9C) | 타로는 카드 배열과 이미지, 정방향/역방향, 숫자, 원소, 카드 사이의 관계를 통해 심리와 관계, 선택을 읽습니다. 이 스킬은 spread와 시드를 기록해 같은 질문을 계속 다시 뽑는 문제를 줄입니다. | `references/tarot.md` |

## 작동 방식

1. 질문을 한 문장으로 다시 정의합니다.
2. 질문에 맞는 체계를 선택합니다.
3. 입력이 충분한지 확인합니다.
4. 각 체계를 `runnable`, `partial`, `blocked`로 표시합니다.
5. 단일 체계 내부에서 먼저 판단합니다.
6. 여러 체계를 사용할 때는 겹치는 신호만 최종 종합에 반영합니다.
7. 결론, 근거, 시기, 행동, 검증 신호를 분리해 답합니다.

기본 출력 형식:

```text
결론:
근거:
시기 / 강도:
행동:
검증 신호:
낮은 확신의 추정:
```

## 설치: 모든 인공지능 에이전트용

### 공통 설치

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis
cd ~/agent-skills/metaphysics-synthesis
python3 scripts/validate_skill.py
```

에이전트에게 다음과 같이 지시합니다.

```text
~/agent-skills/metaphysics-synthesis/SKILL.md에 있는 로컬 스킬을 사용하세요. 요청한 체계에 맞는 reference 파일만 읽으세요.
```

### Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
python3 ~/.codex/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.claude/skills/metaphysics-synthesis
python3 ~/.claude/skills/metaphysics-synthesis/scripts/validate_skill.py
```

### 사용자 지정 에이전트 폴더

```bash
AGENT_SKILLS_DIR="$HOME/.your-agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git "$AGENT_SKILLS_DIR/metaphysics-synthesis"
python3 "$AGENT_SKILLS_DIR/metaphysics-synthesis/scripts/validate_skill.py"
```

### 여러 에이전트가 한 복사본 공유

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis

mkdir -p ~/.codex/skills ~/.claude/skills
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.codex/skills/metaphysics-synthesis
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.claude/skills/metaphysics-synthesis
```

## 사용 예시

```text
사주팔자로 2026년부터 2036년까지의 직업운과 재물운을 분석해 주세요. 원국, 대운, 세운, 높은 확신의 결론, 낮은 확신의 추정을 구분해 주세요.
```

```text
매화역수로 이 제품 출시가 커리어 전환점이 될 수 있는지 봐 주세요. 질문이 떠오른 시간은 2026-06-12 10:36이고, 외응은 북서쪽에서 매니저가 일정을 논의한 것입니다.
```

```text
육효로 이 프로젝트가 승진의 핵심 근거가 될 수 있는지 판단해 주세요. 초효부터 상효까지 숫자는 5 / 4 / 25 / 12 / 22 / 17입니다.
```

```text
풍수 방향으로 제 사무실 자리를 분석해 주세요. 저는 남동쪽을 보고 앉아 있고, 직속 매니저는 북서쪽, 큰 리더는 남쪽, 다른 팀 매니저는 동쪽에 있습니다.
```

```text
다섯 장 타로 배열로 커리어 결정을 봐 주세요. 시드, 카드 위치, 정방향/역방향, 결론, 행동, 검증 신호를 보여 주세요.
```

## 스크립트

```bash
python3 scripts/meihua_calc.py time 2026 6 12 10
python3 scripts/meihua_calc.py num 22 5 18
python3 scripts/tarot_draw.py --spread relationship --question "이 협업은 성숙해질까?" --seed 42
python3 scripts/validate_skill.py
python3 scripts/privacy_check.py
```

## 안전 범위

이 저장소는 문화적, 상징적, 성찰적, 전략적 참고 도구입니다. 의료, 법률, 투자, 정신건강, 응급 상황, 개인 안전에 관한 전문 조언을 대체하지 않습니다. 위험한 주제에서는 직접 증거와 전문가의 판단을 먼저 사용해야 합니다.

## 라이선스

MIT License. 자세한 내용은 [LICENSE](LICENSE)를 참조하세요.

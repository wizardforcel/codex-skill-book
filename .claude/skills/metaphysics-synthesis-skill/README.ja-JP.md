# 形而上学総合スキル

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab)](scripts/)


形而上学総合スキルは、人工知能エージェントが四柱推命、梅花易数、六爻、風水方位分析、タロット解釈を構造的に扱うための再利用可能な スキルパッケージです。これは単なる占いプロンプトではありません。質問を分類し、入力を確認し、適切な体系を選び、結論、根拠、時期、行動、検証ポイントを分けて出力するための手順です。Codex、Claude Code、そしてローカルファイルを参照できる他の人工知能エージェントで利用できます。

人工知能に占術を扱わせると、よく二つの問題が起きます。一つ目は、四柱推命、易占、風水、タロットを同じ雰囲気で混ぜてしまうことです。二つ目は、一つの象徴を過剰に拡大して、検証できない大きな断定にしてしまうことです。このスキルはその逆を目指します。四柱推命は命式構造、大運、年運、仕事、財運、結婚、健康傾向に使います。梅花易数は時刻、数字、外応、近い出来事の動きに使います。六爻は契約、昇進、上司、給与、プロジェクトの成否など具体的な結果に使います。風水は座席、方位、入口、窓、動線、音、視線、背後の支えに使います。タロットは関係性、心理、選択、障害、転換点に使います。

このスキルは明確な結論を出すためのものですが、無理な確定はしません。入力が足りない場合は `runnable`、`partial`、`blocked` として状態を分けます。出生時刻が曖昧なら時柱に関する細部を強く断定しません。六爻の入力順が不明なら納甲の細断を制限します。風水で方位と間取りが不明なら玄空飛星を断定しません。タロットで既にカードが提示されている場合は再抽選せず、人工知能がカードを引く場合はシードを示して再現可能にします。

## 言語

- [英語](README.md)
- [簡体字中国語](README.zh-CN.md)
- [韓国語](README.ko-KR.md)
- [日本語](README.ja-JP.md)
- [フランス語](README.fr-FR.md)
- [スペイン語](README.es-ES.md)

## このスキルが向いている用途

このリポジトリは、人工知能エージェントに占術の「口調」ではなく「手順」を持たせたい人に向いています。毎回長いプロンプトを書かなくても、スキルフォルダをエージェントが読める場所に置けば、エージェントは `SKILL.md` と必要な `references/` ファイルを使って回答できます。また、四柱推命、梅花易数、六爻、風水、タロットを含む相談ツールや自動化ワークフローを作るときの土台にもなります。入力契約、出力テンプレート、計算補助スクリプト、プライバシーチェックが含まれているため、公開用にも内部用にも拡張しやすい構成です。

## 対応体系

| 体系 | 約 100 字の概要 | 主なファイル |
| --- | --- | --- |
| [四柱推命](https://ja.wikipedia.org/wiki/%E5%9B%9B%E6%9F%B1%E6%8E%A8%E5%91%BD) | 四柱推命は生年月日時を年柱、月柱、日柱、時柱として扱い、干支、五行、十神、大運、年運から人生構造を読みます。このスキルでは命式の計算可能な事実と解釈を分け、不確実な出生情報を無理に補いません。 | `references/bazi.md` |
| [梅花易数 / 易経](https://ja.wikipedia.org/wiki/%E6%98%93%E7%B5%8C) | 梅花易数は時刻、数字、外応、方位、音、物象から近い出来事の動きを読む易占の一種です。本卦、動爻、互卦、変卦、体用関係、外応を別々の証拠として扱います。 | `references/meihua.md` |
| [六爻 / 納甲](https://en.wikipedia.org/wiki/Wenwanggua) | 六爻は六本の爻、動爻、世応、六親、六神、月日との関係から具体的な成否を読みます。昇進、契約、上司、給与、プロジェクトなど実務的な質問に向いています。入力不足なら部分判断にします。 | `references/liuyao.md` |
| [風水](https://ja.wikipedia.org/wiki/%E9%A2%A8%E6%B0%B4) | 風水は場所、方位、入口、窓、背後、前方の開け、動線、騒音、視線の圧力を扱います。このスキルは形勢を先に見て、理気や方位象意を後から適用します。高額な開運グッズより実際の環境改善を重視します。 | `references/fengshui.md` |
| [タロット](https://ja.wikipedia.org/wiki/%E3%82%BF%E3%83%AD%E3%83%83%E3%83%88) | タロットはスプレッド、カードの位置、図像、正位置/逆位置、スート、カード同士の関係から心理や選択を読みます。このスキルではシードを示す抽カードを使い、同じ質問を何度も引き直すことを避けます。 | `references/tarot.md` |

## 基本ワークフロー

1. 質問を一文で整理します。
2. どの体系が最も適切かを決めます。
3. 入力が十分かを確認します。
4. 各体系を `runnable`、`partial`、`blocked` に分類します。
5. まず単独体系として整合した判断を出します。
6. 複数体系を使う場合は、重なる信号だけを総合します。
7. 結論、根拠、時期、行動、検証ポイントを分けて出します。

標準出力:

```text
結論:
根拠:
時期 / 強弱:
行動:
検証ポイント:
低確度の推測:
```

## インストール: すべての人工知能エージェント向け

### 共通インストール

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis
cd ~/agent-skills/metaphysics-synthesis
python3 scripts/validate_skill.py
```

エージェントには次のように伝えます。

```text
~/agent-skills/metaphysics-synthesis/SKILL.md のローカルスキルを使用してください。依頼された体系に合う reference ファイルだけを読んでください。
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

### 任意のエージェント用スキルフォルダ

```bash
AGENT_SKILLS_DIR="$HOME/.your-agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git "$AGENT_SKILLS_DIR/metaphysics-synthesis"
python3 "$AGENT_SKILLS_DIR/metaphysics-synthesis/scripts/validate_skill.py"
```

### 複数エージェントで共有

```bash
mkdir -p ~/agent-skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/agent-skills/metaphysics-synthesis

mkdir -p ~/.codex/skills ~/.claude/skills
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.codex/skills/metaphysics-synthesis
ln -sfn ~/agent-skills/metaphysics-synthesis ~/.claude/skills/metaphysics-synthesis
```

## 使用例

```text
この四柱推命の命式について、2026年から2036年までの仕事運と財運を分析してください。命式、大運、年運、高確度の結論、低確度の推測を分けてください。
```

```text
梅花易数で、この製品リリースがキャリア上の突破口になるかを見てください。問いが起きた時刻は 2026-06-12 10:36、外応は北西で上司がスケジュールを話していたことです。
```

```text
六爻で、このプロジェクトが昇進の主な根拠になるか判断してください。初爻から上爻までの数字は 5 / 4 / 25 / 12 / 22 / 17 です。
```

```text
風水方位で私の席を分析してください。私は南東を向いて座り、直属上司は北西、大きなリーダーは南、他チームの責任者は東にいます。
```

```text
五枚のタロットでキャリア上の選択を読んでください。シード、カード位置、正位置/逆位置、結論、行動、検証ポイントを示してください。
```

## スクリプト

```bash
python3 scripts/meihua_calc.py time 2026 6 12 10
python3 scripts/meihua_calc.py num 22 5 18
python3 scripts/tarot_draw.py --spread relationship --question "この協力関係は成熟しますか？" --seed 42
python3 scripts/validate_skill.py
python3 scripts/privacy_check.py
```

## 安全範囲

このリポジトリは文化的、象徴的、内省的、戦略的な参考ツールです。医療、法律、投資、メンタルヘルス、緊急対応、個人の安全に関する専門的助言の代替にはなりません。高リスクの質問では、直接証拠と専門家の判断を優先してください。

## ライセンス

MIT License。詳細は [LICENSE](LICENSE) を参照してください。

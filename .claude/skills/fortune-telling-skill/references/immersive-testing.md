# Immersive Testing and Demo Mode

Use this reference when the user wants a more cinematic or realistic test session with images, animations, screenshots, mood boards, room photos, object photos, palm photos, or video frames.

## Purpose

Make the session feel like a real reading table without pretending that visuals prove destiny. Images and animations are atmosphere and symbolic anchors.

## Supported inputs

- Uploaded images
- Short videos or selected frames
- Screenshots
- Mood boards
- Desk, room, object, candle, cards, notebook, or workspace photos
- README demo assets, such as animated tarot shuffle or spread diagrams

## Session flow

1. Boundary: "这是娱乐性和象征性的解读，不替代专业建议。"
2. Visual grounding: describe visible non-sensitive elements first.
3. Mood choice: ask what kind of atmosphere the user wants: calm, direct, mysterious, practical, gentle, or ritual-heavy.
4. Question calibration: ask two or three targeted questions before drawing or interpreting.
5. Ritual narration: use the visual as a reading table, not as evidence.
6. Reading: connect symbols from the image/animation with cards, elements, or the user's question.
7. Grounding: give practical reflection prompts.

## Prompt examples

```text
用 $fortune-telling 做一次沉浸式塔罗测试。
我会上传一张桌面照片，请你先按画面取象，再像真人咨询一样问我问题，最后洗牌切牌抽牌。
```

```text
用 $fortune-telling 做 README 演示。
请用 assets/tarot-shuffle-animation.svg 的氛围，写一段用户会想尝试的完整塔罗开场。
```

```text
用 $fortune-telling 看这张图片的事业状态。
请先描述你看到的颜色、光线、物件和构图，再把它们作为象征锚点，不要从外貌判断身份或健康。
```

## Visual language

Allowed:

- "这张图的光线偏暗，像是一个收束、整理、等待答案的阶段。"
- "画面中心的物件很清楚，我会把它读成当前问题的焦点。"
- "动画里的牌从散到合，可以作为从混乱到聚焦的象征。"

Avoid:

- "我从照片看出你一定会..."
- "你的脸/手说明你的健康/寿命/财富..."
- "这张图证明对方正在想你..."

## README display guidance

Use lightweight SVG assets so GitHub can display them without external hosting. Animated SVG is suitable for a reading-flow preview, while static SVG is better for diagrams and repository cover images.

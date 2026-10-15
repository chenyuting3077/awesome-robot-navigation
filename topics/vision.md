# 電腦視覺（偵測、分割、視覺基礎模型）

## 在解決的問題

- 開放詞彙：偵測、分割不限類別（CLIP、Grounding DINO、SAM 3）。
- 通用視覺特徵：自監督預訓練（DINO）供深度、匹配、分割等下游任務。
- 即時性：能在機上跑（RT-DETR、YOLO-World）。
- 時序一致：點追蹤、影片分割（CoTracker、SAM 2）。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 來源 |
|---|---|---|---|---|---|
| 2026-04 | [OVS-DINO](https://arxiv.org/abs/2604.08461) | Tongji / PolyU 等 | 結構對齊 SAM 與 DINO 特徵，加語言引導做開放詞彙分割 | arXiv |
| 2026-03 | [dinov3.seg](https://arxiv.org/abs/2603.19531) | IIT Bombay / Monash | 凍結 DINOv3 + 訓練文字編碼器（dinov3.txt），加分割 adapter 做開放詞彙語意分割 | arXiv |
| 2026-02 | [Taming SAM3 in the Wild](https://arxiv.org/abs/2602.06333) | SKKU / SWJTU / NJUST 等 | 用 concept bank 校正 SAM3 的開放詞彙分割預測 | arXiv |

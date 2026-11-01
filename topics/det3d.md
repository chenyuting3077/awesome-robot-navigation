# 3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）

## 在解決的問題

- 點雲骨幹：在大場景上兼顧準確與速度，並靠自監督或 2D 基礎模型蒸餾減少 3D 標註。
- 開放詞彙 3D 偵測與實例分割：3D 標註少，靠 2D 基礎模型（CLIP、SAM）的結果提升到 3D。
- 物件位姿與形狀：從點雲或單張影像估計物件 6D／9D 位姿。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [F2G-Pose](https://arxiv.org/abs/2610.31623) · [專案頁](https://jrryzh.github.io/F2G-Pose/) | Fudan Univ. / Shanghai Innovation Institute | 凍結 RADIO 基礎特徵抬升到局部點雲，單次 feed-forward 同時預測類別層級位姿、尺寸與補全形狀 | SOPE、ROPE 達 SOTA（作者自報）；位姿推論 28 FPS | [GitHub](https://github.com/jrryzh/F2G-Pose) | NeurIPS 2026 |
| 2026-09 | [Co-3DGT](https://arxiv.org/abs/2608.19973) | UESTC / SUTD / Hainan | 開放詞彙 3D 偵測在物件發現階段做共同蒸餾，訓練階段用雙重引導降低不準的框與語意的影響 |  | [GitHub](https://github.com/shangboyuan/Co-3DGT) | ECCV 2026 |

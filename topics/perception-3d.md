# 深度估計與 occupancy

## 在解決的問題

- 單眼公制深度：要有絕對尺度，且相機內參常未知。
- 雙目深度的零樣本泛化。
- 透明、反光表面讓深度感測器失效。
- occupancy：多源自自駕，室內與開放詞彙版本正在補上。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09 | [Monocular Depth Estimation: Progress and Opportunities](https://arxiv.org/abs/2609.01172) | HKU | 單眼深度綜述 |  | [GitHub](https://github.com/CVMI-Lab/Depth_Survey) | arXiv |
| 2026-07 | [The Multipath Blind Spot](https://arxiv.org/abs/2607.04101) | RKMVERI | 在凍結的深度基礎模型上，用稀疏錨點校正出公制深度 |  | 未公開 | arXiv |
| 2026-07 | [ARDepth](https://arxiv.org/abs/2607.12433) | SYSU / Baidu | 自回歸單眼深度估計 |  | 未公開 | arXiv |
| 2026-05 | [Focusable Monocular Depth Estimation](https://arxiv.org/abs/2605.11756) | SJTU / HKUST (GZ) | 區域導向深度：Depth Anything 2/3 負責幾何 + SAM3 選區域（相對深度） |  | 未公開 | arXiv |
| 2026-04 | [FreeOcc](https://arxiv.org/abs/2604.28115) · [專案頁](https://the-masses.github.io/freeocc-web/) | HKUST (GZ) / MBZUAI | 免訓練、具身、開放詞彙 occupancy 預測 |  | [GitHub](https://github.com/the-masses/FreeOcc) | arXiv |

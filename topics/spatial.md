# 3D 空間理解（3D grounding、空間推理 VLM、3D-LLM）

## 在解決的問題

- 3D grounding：把「沙發右邊的桌子」這類含空間關係的描述對到 3D 中的特定物件。
- VLM 的空間推理：VLM 多用 2D 圖文訓練，距離、方位、大小常答錯；做法是用 3D 資料合成空間問答，或接上深度、點雲輸入。
- 從影片理解空間：機器人只有連續影像、沒有完整點雲時，要從影片累積對空間的記憶與推理。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | [Stream3D-VLM](https://arxiv.org/abs/2606.06891) · [專案頁](https://stream3d-vlm.github.io/) | Zhejiang / Tencent Hunyuan / HKUST | 串流影像的線上 3D VLM：用自迴歸方式學何時該回答，並逐步注入對齊時間的幾何先驗 | 資料集超過 100 萬組 QA、29 種任務 | [GitHub](https://github.com/hanxunyu/Stream3D-VLM) | ECCV 2026 |
| 2025-12 | [OpenGround](https://arxiv.org/abs/2512.23020) · [專案頁](https://why-102.github.io/openground.io/) | Nanjing / China Mobile | 不靠預先定義的物件查找表，以任務鏈規劃並線上感知目標，處理未定義目標與複雜查詢 | OpenTarget 提升 17.6% | [GitHub](https://github.com/why-102/openground) | ECCV 2026 |
| 2026-10 | [ClusterSplat](https://arxiv.org/abs/2610.36462) · [專案頁](https://jaesung8.github.io/clustersplat/) | KAIST | 在 3DGS 中做 3D grounding，不用閾值或 top-ratio 過濾，改以語意叢集選出目標 Gaussian，同時輸出 2D 遮罩與 3D Gaussian 集合 | ScanRefer 3D mIoU 23.33、mAcc@0.25 43.38（作者稱優於 LangSplat、OpenGaussian） | 未公開 | NeurIPS 2026 |
| 2026-10 | [P³-VLM](https://arxiv.org/abs/2610.28018) · [專案頁](https://p3vlm.insait.ai/) | INSAIT, Sofia Univ. | 指出 3D VLM 依賴 bounding box 造成語意洩漏，改用單一 3D 點當 prompt，三路徑（位置、任務、情境）架構、不需偵測器 | 點提示下 location-grounded captioning 52.1%（作者稱 SOTA）；盲 LLM 在 Nr3D 從 36.4% 降到 18.0% | 未公開 | NeurIPS 2026 |

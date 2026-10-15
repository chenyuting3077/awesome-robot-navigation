# 3D 感知（深度、feed-forward 重建、occupancy）

## 在解決的問題

- 單眼公制深度：要有絕對尺度，且相機內參常未知。
- feed-forward 重建：不跑 SfM 優化，一次前向得到相機與幾何；挑戰在大規模與串流輸入。
- 雙目深度的零樣本泛化。
- 3D 表示：3DGS 取代 NeRF，可即時渲染。
- occupancy：多源自自駕，提供規劃用的 3D 佔據。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 來源 |
|---|---|---|---|---|---|
| 2026-09 | [Scal3R](https://arxiv.org/abs/2609.04201) | | 多相對位姿 query 做可擴展的線上 3D 重建 | arXiv |
| 2026-09 | [Monocular Depth Estimation: Progress and Opportunities](https://arxiv.org/abs/2609.01172) | | 單眼深度綜述 | arXiv |
| 2026-08 | [GeoFF3D](https://arxiv.org/abs/2608.28288) | | 座標錨定的 feed-forward 重建，用於大尺度 UAV 建圖 | arXiv |
| 2026-07 | [The Multipath Blind Spot](https://arxiv.org/abs/2607.04101) | | 在凍結的深度基礎模型上，用稀疏錨點校正出公制深度 | arXiv |
| 2026-07 | [ARDepth](https://arxiv.org/abs/2607.12433) | | 自回歸單眼深度估計 | arXiv |
| 2026-05 | [Focusable Monocular Depth Estimation](https://arxiv.org/abs/2605.11756) | | 區域導向深度：Depth Anything 2/3 負責幾何 + SAM3 選區域（相對深度） | arXiv |
| 2026-04 | [FreeOcc](https://arxiv.org/abs/2604.28115) | | 免訓練、具身、開放詞彙 occupancy 預測 | arXiv |
| 2026-04 | [Feed-forward 3D scene modeling survey](https://arxiv.org/abs/2604.14025) | | feed-forward 3D 重建綜述，涵蓋 Point3R、IncVGGT、ZipMap 等串流／增量版本 | arXiv |
| 2026-02 | [VGG-T³](https://arxiv.org/abs/2602.23361) | | 大規模離線 feed-forward 重建 | arXiv |
| 2025-11 | [AMB3R](https://arxiv.org/abs/2511.20343) | | feed-forward 公制尺度重建 + 稀疏體素後端，不微調即可延伸到 VO／SLAM（CVPR 2026） | arXiv |
| 2025-11 | [Depth Anything 3](https://arxiv.org/abs/2511.10647) | ByteDance | 深度基礎模型 | arXiv |

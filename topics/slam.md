# SLAM 與定位

## 在解決的問題

- 退化場景：長廊、隧道、空曠處 LiDAR 或視覺特徵不足。
- 多感測器緊耦合：LiDAR、IMU、相機融合。
- 學習式前端：用 DROID、MASt3R、VGGT 等取代手工特徵，處理無紋理、免校正相機。
- 稠密且寫實的地圖：NeRF／3DGS SLAM。
- 大尺度、長期：回環、地點辨識、多機器人、場景隨時間變化。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [Line-Augmented cuVSLAM](https://arxiv.org/abs/2610.20958) | Analog Devices、NVIDIA | 在 NVIDIA cuVSLAM 加線特徵（Plücker 參數化、點線殘差進 Gauss-Newton 位姿解與滑窗 BA），點特徵稀少時自動加重線的權重，針對倉庫等低紋理場景 | RGB-D：TUM Freiburg3 22 條序列 ATE 降 38.5%，Replica 8 條降 30.1% | 未公開 | arXiv |
| 2026-09 | [Scal3R](https://arxiv.org/abs/2609.04201) · [專案頁](https://linjohnss.github.io/scal3r/) | NYCU / NVIDIA | 凍結 CUT3R、STream3R 骨幹，只加約 1% 參數的位姿 token 對多個過去關鍵幀並行查相對位姿，再以線上位姿圖與回環融合，長影片不再累積漂移 | KITTI 平均 ATE 比線上基線降 60% 以上；回環示範 ATE 49.8 m → 6.4 m | [GitHub](https://github.com/NVlabs/scal3r) | ECCV 2026 |
| 2026-09 | [FFVO](https://arxiv.org/abs/2609.13733) | Waymo / UW | feed-forward 位姿解碼器做長距離 VO |  | 未公開 | arXiv |
| 2026-04 | [BIEVR-LIO](https://arxiv.org/abs/2604.14421) | ETH ASL / RSL | 幾何資訊貧乏場景，用 bump image 強化 voxel map，不需額外感測器 |  | [GitHub](https://github.com/ethz-asl/BIEVR-LIO) | arXiv |
| 2026-01 | [VGGT-SLAM 2.0](https://arxiv.org/abs/2601.19887) | MIT SPARK | 新 factor graph 設計消除子地圖對齊的 15-DoF 漂移與平面退化；直接用 VGGT attention 層驗證回環，不需額外訓練 | TUM 位姿誤差比 VGGT-SLAM 低約 23%；Jetson Thor 地面機器人即時運行 | [GitHub](https://github.com/MIT-SPARK/VGGT-SLAM) | RSS 2026 |

# SLAM 與定位

## 在解決的問題

- 退化場景：長廊、隧道、空曠處 LiDAR 或視覺特徵不足。
- 多感測器緊耦合：LiDAR、IMU、相機融合。
- 學習式前端：用 DROID、MASt3R、VGGT 等取代手工特徵，處理無紋理、免校正相機。
- 稠密且寫實的地圖：NeRF／3DGS SLAM。
- 大尺度、長期：回環、地點辨識、多機器人、場景隨時間變化。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 來源 |
|---|---|---|---|---|---|
| 2026-09 | [AMB3R-SLAM](https://arxiv.org/abs/2609.19518) | UCL | 單眼即時 SLAM，輕量前端 + 局部／中層／全域三層後端；不做 BA，所以不依賴靜態場景假設；也可吃雙目、RGB-D、LiDAR | 單張消費級 GPU 跑超過 1 萬幀；VBR、Oxford Spires ATE 比前 SOTA 低 70% 以上；加 LiDAR 後 KITTI、VBR 誤差小於 1 m | arXiv |
| 2026-09 | [VGGT-GS SLAM](https://arxiv.org/abs/2609.19628) | NUS | 免校正單眼 3DGS SLAM，用 VGGT 的位姿與深度初始化子地圖，再聯合優化位姿、地圖、內參 | arXiv |
| 2026-09 | [Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM](https://arxiv.org/abs/2609.36753) | Sookmyung Women's Univ. | 處理隧道、管道這類沿軸向特徵貧乏、LiDAR odometry 會漂移的場景 | arXiv |
| 2026-09 | [FFVO](https://arxiv.org/abs/2609.13733) | Waymo / UW | feed-forward 位姿解碼器做長距離 VO | arXiv |
| 2026-06 | [ScaRF-SLAM](https://arxiv.org/abs/2606.00307) | Oxford ORI / Georgia Tech | feed-forward 重建 + 傳統視覺 SLAM，解尺度一致性 | RA-L 2026 |
| 2026-06 | [Ultra-Fusion](https://arxiv.org/abs/2606.21223) | BIT / SJTU 等 | 感測器退化與時空擾動下的緊耦合多感測器融合 SLAM | arXiv |
| 2026-04 | [RMGS-SLAM](https://arxiv.org/abs/2604.12942) | NUS / Sichuan Univ. | 緊耦合 LiDAR-慣性-視覺 3DGS SLAM，大尺度戶外即時定位 + 寫實建圖 | arXiv |
| 2026-04 | [Environment-Adaptive Solid-State LIO](https://arxiv.org/abs/2604.15864) | CQUPT / Chulalongkorn / HDU | 固態 LiDAR 慣性里程計，處理極端環境的幾何退化 | arXiv |
| 2026-04 | [BIEVR-LIO](https://arxiv.org/abs/2604.14421) | ETH ASL / RSL | 幾何資訊貧乏場景，用 bump image 強化 voxel map，不需額外感測器 | arXiv |
| 2026-04 | [HyVGGT-VO](https://arxiv.org/abs/2604.02107) | Beihang | feed-forward 模型與傳統最佳化緊耦合的稠密 VO | arXiv |
| 2026-03 | [Degeneracy-Resilient Teach and Repeat](https://arxiv.org/abs/2603.10248) | Univ. of Toronto | 用 FMCW LiDAR 在幾何退化環境做 teach & repeat | arXiv |
| 2026-01 | [VGGT-SLAM 2.0](https://arxiv.org/abs/2601.19887) | MIT SPARK | 新 factor graph 設計消除子地圖對齊的 15-DoF 漂移與平面退化；直接用 VGGT attention 層驗證回環，不需額外訓練 | TUM 位姿誤差比 VGGT-SLAM 低約 23%；Jetson Thor 地面機器人即時運行 | RSS 2026 |

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
| 2026-10 | [LIN-SLAM](https://arxiv.org/abs/2610.21199) | Beihang Univ. | 幾何 LiDAR-IMU 高頻估計接神經隱式追蹤、持續建圖與全域優化，讓神經隱式 SLAM 能在機上即時跑 | 12 條序列（32／64／128 線）平均 ATE 最低；Unitree Go2 + Jetson Orin NX 跑 1.47 km 室內，終點閉合誤差 0.141 m | 未公開 | arXiv |
| 2026-09 | [AMB3R-SLAM](https://arxiv.org/abs/2609.19518) · [專案頁](https://hengyiwang.github.io/projects/amber-slam) | UCL | 單眼即時 SLAM，輕量前端 + 局部／中層／全域三層後端；不做 BA，所以不依賴靜態場景假設；也可吃雙目、RGB-D、LiDAR | 單張消費級 GPU 跑超過 1 萬幀；VBR、Oxford Spires ATE 比前 SOTA 低 70% 以上；加 LiDAR 後 KITTI、VBR 誤差小於 1 m | [GitHub](https://github.com/HengyiWang/amb3r-slam) | arXiv |
| 2026-09 | [VGGT-GS SLAM](https://arxiv.org/abs/2609.19628) | NUS | 免校正單眼 3DGS SLAM，用 VGGT 的位姿與深度初始化子地圖，再聯合優化位姿、地圖、內參 |  | 未公開 | arXiv |
| 2026-09 | [Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM](https://arxiv.org/abs/2609.36753) | Sookmyung Women's Univ. | 處理隧道、管道這類沿軸向特徵貧乏、LiDAR odometry 會漂移的場景 |  | 未公開 | arXiv |
| 2026-09 | [FFVO](https://arxiv.org/abs/2609.13733) | Waymo / UW | feed-forward 位姿解碼器做長距離 VO |  | 未公開 | arXiv |
| 2026-06 | [ScaRF-SLAM](https://arxiv.org/abs/2606.00307) | Oxford ORI / Georgia Tech | feed-forward 重建 + 傳統視覺 SLAM，解尺度一致性 |  | [GitHub](https://github.com/ori-drs/ScaRF-SLAM) | RA-L 2026 |
| 2026-06 | [Ultra-Fusion](https://arxiv.org/abs/2606.21223) · [專案頁](https://sjtuyinjie.github.io/ultrafusion-web/) | BIT / SJTU 等 | 感測器退化與時空擾動下的緊耦合多感測器融合 SLAM |  | [GitHub](https://github.com/sjtuyinjie/Ultra-Fusion) | arXiv |
| 2026-04 | [RMGS-SLAM](https://arxiv.org/abs/2604.12942) | NUS / Sichuan Univ. | 緊耦合 LiDAR-慣性-視覺 3DGS SLAM，大尺度戶外即時定位 + 寫實建圖 |  | 未公開 | arXiv |
| 2026-04 | [Environment-Adaptive Solid-State LIO](https://arxiv.org/abs/2604.15864) | CQUPT / Chulalongkorn / HDU | 固態 LiDAR 慣性里程計，處理極端環境的幾何退化 |  | 未公開 | arXiv |
| 2026-04 | [BIEVR-LIO](https://arxiv.org/abs/2604.14421) | ETH ASL / RSL | 幾何資訊貧乏場景，用 bump image 強化 voxel map，不需額外感測器 |  | [GitHub](https://github.com/ethz-asl/BIEVR-LIO) | arXiv |
| 2026-04 | [HyVGGT-VO](https://arxiv.org/abs/2604.02107) · [專案頁](https://geneta2580.github.io/HyVGGT-VO.io) | Beihang | feed-forward 模型與傳統最佳化緊耦合的稠密 VO |  | [GitHub](https://github.com/Geneta2580/HyVGGT-VO) | arXiv |
| 2026-03 | [Degeneracy-Resilient Teach and Repeat](https://arxiv.org/abs/2603.10248) | Univ. of Toronto | 用 FMCW LiDAR 在幾何退化環境做 teach & repeat |  | 未公開 | arXiv |
| 2026-01 | [VGGT-SLAM 2.0](https://arxiv.org/abs/2601.19887) | MIT SPARK | 新 factor graph 設計消除子地圖對齊的 15-DoF 漂移與平面退化；直接用 VGGT attention 層驗證回環，不需額外訓練 | TUM 位姿誤差比 VGGT-SLAM 低約 23%；Jetson Thor 地面機器人即時運行 | [GitHub](https://github.com/MIT-SPARK/VGGT-SLAM) | RSS 2026 |

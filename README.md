# Robot Nav Survey

AMR、四足、輪足機器人的導航、視覺、3D 感知、SLAM 與 Real2Sim 前沿論文整理，每三天自動更新。

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/ 或 digests/ 後重跑 -->

- 每三天由排程 agent 依 [CLAUDE.md](CLAUDE.md) 的規則搜尋新論文並開 PR，審過再 merge。
- 手動更新：在 repo 裡開 Claude Code，說「更新論文整理」。

最後更新：2026-10-15

## 目錄

- [本月趨勢（2026-10）](#本月趨勢2026-10)
- [VLN 與導航基礎模型](#vln-與導航基礎模型)
- [局部導航策略（diffusion / world model）](#局部導航策略diffusion--world-model)
- [語意地圖與場景圖](#語意地圖與場景圖)
- [四足](#四足)
- [輪足（雙足輪、四足輪）](#輪足雙足輪四足輪)
- [SLAM 與定位](#slam-與定位)
- [3D 感知（深度、feed-forward 重建、occupancy）](#3d-感知深度feed-forward-重建occupancy)
- [電腦視覺（偵測、分割、視覺基礎模型）](#電腦視覺偵測分割視覺基礎模型)
- [Real2Sim 場景還原](#real2sim-場景還原)
- [月報](#月報)

## 本月趨勢（2026-10）

- 觀察：VLN 往「慢 VLM 給影像錨點 + 快 waypoint 層」雙層架構走（ABot-N1、Robostral Navigate），且開始只用單眼 RGB。
- 觀察：局部導航從 diffusion policy 轉向 world model（LiteNWM、NavWM、NavWAM、UniNav）。
- 觀察：雙足輪研究多停在運動控制，與語言導航結合的很少。
- 觀察：SLAM 大量改用 VGGT 類 feed-forward 模型當前端（VGGT-SLAM 2.0、AMB3R-SLAM、VGGT-GS SLAM），後端仍是 factor graph 或分層優化。
- 觀察：Real2Sim 從「重建出能看的場景」走向「能互動的場景」（ArtiTwinSplat 輸出 URDF 關節並匯入 Isaac Sim）。
- 推測：單眼 RGB 方案能否上 AMR 取決於機上算力；可量 Jetson 上推論延遲驗證。

## VLN 與導航基礎模型

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-07 | [Robostral Navigate](https://arxiv.org/abs/2607.20785) | Mistral AI | 8B VLM 只用單眼 RGB，在畫面上指出下一個目標點；目標不在視野時輸出局部座標位移 | R2R-CE val-unseen SR 76.6%；online RL +3.2% | 摘要 |
| 2026-07 | [ABot-N1](https://arxiv.org/abs/2607.10383) | Alibaba AMAP | 慢 VLM 推理出影像錨點，快模組轉成連續 waypoint；同一架構做 point/object/POI/指令/跟人五種任務 | 室內 95.4%、室外 92.9% SR；POI 抵達 77.3% | 摘要 |
| 2026-07 | [GemNav](https://arxiv.org/abs/2607.06882) | | MLLM 輸出離散 token 當導航動作 | | 標題 |
| 2026-04 | [Robot Navigation via Foundation Language Models: A Review](https://dl.acm.org/doi/10.1145/3802539) | | ACM CSUR 綜述 | | 標題 |
| 2024-12 | [NaVILA](https://arxiv.org/abs/2412.04453) | UCSD / NVIDIA / USC | VLM 輸出中層語言動作，低層運動策略執行；換低層策略即可換機體 | 實機 25 指令 88% SR | 摘要 |

## 局部導航策略（diffusion / world model）

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 摘要 |
| 2026-08 | [UniNav](https://arxiv.org/abs/2608.03244) | | 統一 world-action diffusion | | 標題 |
| 2026-08 | [ODG-NoMaD](https://arxiv.org/abs/2608.21395) | | NoMaD 加俯視相機方向引導 | | 標題 |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) | | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） | | 標題 |
| 2026-06 | [NavWM](https://arxiv.org/abs/2606.24101) | | 導航 world model 做前瞻規劃 | | 標題 |
| 2026-06 | [NavWAM](https://arxiv.org/abs/2606.13494) | | goal-conditioned world action model | | 標題 |
| 2026-05 | [NavOL](https://arxiv.org/abs/2605.11762) | | diffusion 導航策略在 IsaacLab 線上模仿學習，解 NavDP 離線資料限制 | | 標題 |
| 2026-03 | [Beyond Imitation](https://arxiv.org/abs/2603.12868) | | RL 微調 diffusion 導航策略 | | 標題 |
| 2025-05 | [NavDP](https://arxiv.org/abs/2505.08712) | | 純模擬訓練 + 特權資訊引導，zero-shot sim-to-real 跨機體 | | 摘要 |

## 語意地圖與場景圖

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-05 | [LEXI-SG](https://arxiv.org/abs/2605.13741) | Oxford | 只用單眼 RGB 建開放詞彙 3D 場景圖，以房間為單位 feed-forward 重建（RA-L 2026） | 評估在 HM3D 與自錄辦公室序列，未做實機導航 | 摘要 |
| 2026-03 | [OGScene3D](https://arxiv.org/abs/2603.16301) | | 邊探索邊增量建場景圖，confidence-aware Gaussian 語意表示 | | 摘要 |
| 2024-03 | [HOV-SG](https://arxiv.org/abs/2403.17846) | Freiburg | 樓層／房間／物件階層，跨樓層 Voronoi 圖導航（RSS 2024） | 比稠密開放詞彙地圖小 75% | 摘要 |

## 四足

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-07 | [APT-RL: Agile perceptive multi-skill locomotion](https://arxiv.org/abs/2607.13579) | KAIST 等 | 軌跡最佳化 8 分鐘產生 18 萬條動作先驗，再用 RL + 機載感知適應 3D 地形（Science Robotics 2026） | 單一策略過樓梯／欄／踏石／溝；瞬間最高 6 m/s | 摘要 |
| 2026-06 | [Perceptive Platform Adaptive Locomotion](https://arxiv.org/abs/2606.25179) | | 感知只給 critic，感知有雜訊時比完全感知策略穩 | | 摘要 |
| 2026-06 | [GUIDE](https://arxiv.org/abs/2606.10832) | | 端到端腿式導航 | | 標題 |
| 2026-04 | [HiPAN](https://arxiv.org/abs/2604.26504) | | 非結構 3D 環境的姿態自適應分層導航 | | 標題 |

## 輪足（雙足輪、四足輪）

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-08 | [Traversal Risk Graph Planning](https://arxiv.org/abs/2608.16433) | | 考慮機身的穿越風險圖規劃 | | 標題 |
| 2026-06 | [Go2-W Long-Distance Navigation](https://arxiv.org/abs/2606.21387) | | 輪子驅動會讓髖關節過熱，訓練能分散負載的策略 | Tsukuba Challenge 2025 自主約 2.8 km（人行道、公園、樓梯） | 摘要 |
| 2026-04 | [Reflexive Obstacle Evasion](https://arxiv.org/abs/2604.23761) | | 輪足高動態反射式閃避 | | 標題 |
| 2026-02 | [Sparse MoE multi-mode locomotion](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1788395/full) | | 雙足輪；稀疏 MoE RL，在滾動與越障間自動切換（Frontiers 2026） | | 摘要 |
| 2024-05 | [Learning Robust Autonomous Navigation and Locomotion for Wheeled-Legged Robots](https://arxiv.org/abs/2405.01792) | ETH | 都市環境公里級自主任務（Science Robotics 2024） | | 摘要 |

## SLAM 與定位

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-09 | [AMB3R-SLAM](https://arxiv.org/abs/2609.19518) | | 單眼即時 SLAM，輕量前端 + 局部／中層／全域三層後端；不做 BA，所以不依賴靜態場景假設；也可吃雙目、RGB-D、LiDAR | 單張消費級 GPU 跑超過 1 萬幀；VBR、Oxford Spires ATE 比前 SOTA 低 70% 以上；加 LiDAR 後 KITTI、VBR 誤差小於 1 m | 摘要 |
| 2026-09 | [VGGT-GS SLAM](https://arxiv.org/abs/2609.19628) | | 免校正單眼 3DGS SLAM，用 VGGT 的位姿與深度初始化子地圖，再聯合優化位姿、地圖、內參 | | 摘要 |
| 2026-09 | [Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM](https://arxiv.org/abs/2609.36753) | | 處理隧道、管道這類沿軸向特徵貧乏、LiDAR odometry 會漂移的場景 | | 摘要 |
| 2026-09 | [FFVO](https://arxiv.org/abs/2609.13733) | | feed-forward 位姿解碼器做長距離 VO | | 標題 |
| 2026-06 | [ScaRF-SLAM](https://arxiv.org/abs/2606.00307) | | feed-forward 重建 + 傳統視覺 SLAM，解尺度一致性 | | 標題 |
| 2026-06 | [Ultra-Fusion](https://arxiv.org/abs/2606.21223) | | 感測器退化與時空擾動下的緊耦合多感測器融合 SLAM | | 標題 |
| 2026-04 | [RMGS-SLAM](https://arxiv.org/abs/2604.12942) | | 緊耦合 LiDAR-慣性-視覺 3DGS SLAM，大尺度戶外即時定位 + 寫實建圖 | | 摘要 |
| 2026-04 | [Environment-Adaptive Solid-State LIO](https://arxiv.org/abs/2604.15864) | | 固態 LiDAR 慣性里程計，處理極端環境的幾何退化 | | 摘要 |
| 2026-04 | [BIEVR-LIO](https://arxiv.org/abs/2604.14421) | | 幾何資訊貧乏場景，用 bump image 強化 voxel map，不需額外感測器 | | 摘要 |
| 2026-04 | [HyVGGT-VO](https://arxiv.org/abs/2604.02107) | | feed-forward 模型與傳統最佳化緊耦合的稠密 VO | | 標題 |
| 2026-03 | [Degeneracy-Resilient Teach and Repeat](https://arxiv.org/abs/2603.10248) | | 用 FMCW LiDAR 在幾何退化環境做 teach & repeat | | 標題 |
| 2026-01 | [VGGT-SLAM 2.0](https://arxiv.org/abs/2601.19887) | MIT SPARK | 新 factor graph 設計消除子地圖對齊的 15-DoF 漂移與平面退化；直接用 VGGT attention 層驗證回環，不需額外訓練（RSS 2026） | TUM 位姿誤差比 VGGT-SLAM 低約 23%；Jetson Thor 地面機器人即時運行 | 摘要 |

## 3D 感知（深度、feed-forward 重建、occupancy）

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-09 | [Scal3R](https://arxiv.org/abs/2609.04201) | | 多相對位姿 query 做可擴展的線上 3D 重建 | | 標題 |
| 2026-09 | [Monocular Depth Estimation: Progress and Opportunities](https://arxiv.org/abs/2609.01172) | | 單眼深度綜述 | | 摘要 |
| 2026-08 | [GeoFF3D](https://arxiv.org/abs/2608.28288) | | 座標錨定的 feed-forward 重建，用於大尺度 UAV 建圖 | | 標題 |
| 2026-07 | [The Multipath Blind Spot](https://arxiv.org/abs/2607.04101) | | 在凍結的深度基礎模型上，用稀疏錨點校正出公制深度 | | 摘要 |
| 2026-07 | [ARDepth](https://arxiv.org/abs/2607.12433) | | 自回歸單眼深度估計 | | 標題 |
| 2026-05 | [Focusable Monocular Depth Estimation](https://arxiv.org/abs/2605.11756) | | 區域導向深度：Depth Anything 2/3 負責幾何 + SAM3 選區域（相對深度） | | 摘要 |
| 2026-04 | [FreeOcc](https://arxiv.org/abs/2604.28115) | | 免訓練、具身、開放詞彙 occupancy 預測 | | 標題 |
| 2026-04 | [Feed-forward 3D scene modeling survey](https://arxiv.org/abs/2604.14025) | | feed-forward 3D 重建綜述，涵蓋 Point3R、IncVGGT、ZipMap 等串流／增量版本 | | 摘要 |
| 2026-02 | [VGG-T³](https://arxiv.org/abs/2602.23361) | | 大規模離線 feed-forward 重建 | | 標題 |
| 2025-11 | [AMB3R](https://arxiv.org/abs/2511.20343) | | feed-forward 公制尺度重建 + 稀疏體素後端，不微調即可延伸到 VO／SLAM（CVPR 2026） | | 摘要 |
| 2025-11 | [Depth Anything 3](https://arxiv.org/abs/2511.10647) | ByteDance | 深度基礎模型 | | 標題 |

## 電腦視覺（偵測、分割、視覺基礎模型）

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-04 | [OVS-DINO](https://arxiv.org/abs/2604.08461) | | 結構對齊 SAM 與 DINO 特徵，加語言引導做開放詞彙分割 | | 標題 |
| 2026-03 | [dinov3.seg](https://arxiv.org/abs/2603.19531) | | 凍結 DINOv3 + 訓練文字編碼器（dinov3.txt），加分割 adapter 做開放詞彙語意分割 | | 摘要 |
| 2026-02 | [Taming SAM3 in the Wild](https://arxiv.org/abs/2602.06333) | | 用 concept bank 校正 SAM3 的開放詞彙分割預測 | | 摘要 |

## Real2Sim 場景還原

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-10 | [Digital Twin-Driven Real2Sim2Real](https://arxiv.org/abs/2610.08339) | | 自駕場景成對重建，以模擬器條件生成訓練影像（非物理互動場景） | | 摘要 |
| 2026-09 | [ReVeal](https://arxiv.org/abs/2609.23910) | | 考慮重建品質的 real-to-sim VLA 策略評估 | | 標題 |
| 2026-06 | [ArtiTwinSplat](https://arxiv.org/abs/2606.24628) | | 手持 RGB-D 影片重建可互動數位分身（3DGS），輸出碰撞網格、門／抽屜關節、URDF，可直接匯入 Isaac Sim | | 摘要 |
| 2026-06 | [Robots Need More than VLA and World Models](https://arxiv.org/abs/2606.06556) | | 立場論文；整理 3DGS 模擬器訓練的導航策略可 zero-shot 轉移到實機（SOUS VIDE、SINGER、GRaD-Nav） | | 摘要 |
| 2026-03 | [SimRecon](https://arxiv.org/abs/2603.02133) | | 從真實影片做 SimReady 的組合式場景重建 | | 標題 |
| 2025-12 | [PolaRiS](https://arxiv.org/abs/2512.16881) | | 可擴展的 real-to-sim 通用策略評估 | | 標題 |
| 2025-09 | [EmbodiedSplat](https://arxiv.org/abs/2509.17430) | | 手機掃描建 3DGS 場景，在 Habitat-Sim 裡微調導航策略後部署回實機 | | 摘要 |
| 2025-02 | [VR-Robo](https://arxiv.org/abs/2502.01536) | | 視覺導航與運動控制的 real-to-sim-to-real 框架 | | 標題 |

## 月報

- [2026-10](digests/2026-10.md)

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 後重跑 -->

# 封存區

從重要論文移出但保留備查，規則見 [README](../README.md#怎樣算重要論文)，共 85 篇。

## VLN 與導航基礎模型：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2024 | [MiniVLN](https://arxiv.org/abs/2409.18800) | CASIA | 兩階段漸進式知識蒸餾，小模型保有 VLN 表現以利部署 | ICRA 2025 | 10 | 未公開 |
| 新興 | 獲獎 | 2023 | [Dynamic Navigation Goal from Dialogue](https://doi.org/10.1109/IROS55552.2023.10342509) | Shanghai Inst. of Tech. / Tsinghua 等 | 從自然語言對話中抽取會移動的目標（如人）的位置作為導航目標 | IROS 2023 | 7 | 未公開 |

## VLN 與導航基礎模型：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用 | 2022 | [ZSON](https://arxiv.org/abs/2206.12403) | Georgia Tech | CLIP 目標嵌入讓 ImageNav 策略零樣本找物件 | NeurIPS 2022 | 352 | [110](https://github.com/gunagg/zson) |
| 主流 | 引用 | 2021 | [EmbCLIP](https://arxiv.org/abs/2111.09888) | AI2 | 只換 CLIP 視覺骨幹不加任務設計就超越多項導航基線 | CVPR 2022 | 304 | [131](https://github.com/allenai/embodied-clip) |
| 主流 | 引用 | 2023 | [GOAT](https://arxiv.org/abs/2311.06430) | UIUC / CMU / Georgia Tech 等 | 多模態目標、終身記憶的通用導航系統，實機長時間部署 | RSS 2024 | 164 | 未公開 |
| 主流 | 引用 | 2023 | [LGX](https://arxiv.org/abs/2303.03480) | UMD | LLM 序列決策加開放詞彙偵測找語言描述的目標物 | RA-L 2024 | 163 | [72](https://github.com/vdorbala/LGX) |
| 主流 | 引用 | 2023 | [PixNav](https://arxiv.org/abs/2309.10309) · [專案頁](https://sites.google.com/view/pixnav/) | Southeast Univ. / PKU / Shanghai AI Lab | 以像素為目標的導航技能銜接基礎模型與底層移動 | ICRA 2024 | 152 | [139](https://github.com/wzcai99/Pixel-Navigator) |
| 主流 | 引用 | 2024 | [Mobility VLA](https://arxiv.org/abs/2407.07775) | Google DeepMind | 長脈絡 VLM 看導覽影片建拓撲圖，再照多模態指令導航 | CoRL 2024 | 103 | 未公開 |
| 主流 | 引用 | 2024 | [HNR](https://arxiv.org/abs/2404.01943) | ICT-CAS / UCAS | 神經輻射表示預測候選點未來特徵做前瞻探索 | CVPR 2024 | 94 | [110](https://github.com/MrZihan/HNR-VLN) |
| 主流 | 引用、獲獎 | 2024 | [PoliFormer](https://arxiv.org/abs/2406.20083) · [專案頁](https://poliformer.allen.ai) | AI2 | 大規模 RL 訓練 Transformer 策略，RGB 直接轉實機 | CoRL 2024 | 89 | [106](https://github.com/allenai/PoliFormer) |
| 主流 | 引用 | 2024 | [GOAT (causal VLN)](https://arxiv.org/abs/2404.10241) | Tongji | 因果推論去除視覺、語言、歷史中的資料偏差 | CVPR 2024 | 86 | [104](https://github.com/CrystalSixone/VLN-GOAT) |
| 主流 | 引用 | 2025 | [SmartWay](https://arxiv.org/abs/2503.10069) · [專案頁](https://sxyxs.github.io/smartway/) | Adelaide | 強化路徑點預測器加可回溯的 MLLM 導航器 | IROS 2025 | 41 | [20](https://github.com/sxyxs/SmartWay-Code) |
| 主流 | 引用 | 2025 | [BeliefMapNav](https://arxiv.org/abs/2506.06487) | SJTU / UMich | 3D 體素信念地圖估計目標分布，結合序列路徑規劃 | NeurIPS 2025 | 34 | [51](https://github.com/ZiboKNOW/BeliefMapNav) |
| 主流 | 引用 | 2025 | [OpenIN](https://arxiv.org/abs/2501.04279) · [專案頁](https://openin-nav.github.io) | BIT | 載體關係場景圖追蹤會移動的物件實例 | RA-L 2025 | 31 | 未公開 |
| 主流 | 引用 | 2025 | [MoRE](https://arxiv.org/abs/2503.08007) | Zhejiang / Westlake / Monash 等 | 多 LoRA 專家 VLA 搭配 RL 微調，用混合品質資料 | ICRA 2025 | 30 | 未公開 |
| 新興 | 獲獎 | 2022 | [ViKiNG](https://arxiv.org/abs/2202.11271) · [專案頁](https://sites.google.com/view/viking-release) | UC Berkeley | 學習式局部可通行性加上衛星圖、路網等地理提示做啟發式搜尋，實機走到公里級目標 | RSS 2022 | 115 | 未公開 |
| 新興 | 獲獎 | 2025 | [SocialNav](https://arxiv.org/abs/2511.21135) · [專案頁](https://amap-eai.github.io/SocialNav/) | Amap Alibaba | 「大腦-動作」階層架構，以 700 萬筆 SocNav 資料訓練遵守社會規範的導航基礎模型 | CVPR 2026 | 22 | [137](https://github.com/AMAP-EAI/SocialNav) |

## 局部導航與規劃（diffusion / world model / 探索）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2023 | [Sequential Neural Barriers](https://arxiv.org/abs/2307.03015) | （論文未列單位） | 依序學習神經控制障壁函數，動態障礙物數量增加時仍能擴展且對分布漂移較穩 | IROS 2023 | 29 | 未公開 |
| 新興 | 獲獎 | 2022 | [Confidence-based Nav under Occlusion](https://doi.org/10.1109/ICRA46639.2022.9812090) | KAIST | 感測器被髒污遮擋時，以信心度驅動 RL 主動探索確保可見度 | ICRA 2022 | 12 | 未公開 |
| 新興 | 獲獎 | 2024 | [Hiking Trail Navigation](https://arxiv.org/abs/2409.15671) | West Virginia University | 語意分割判斷步道、幾何分析判斷可通行，必要時可離開步道 | IROS 2025 | 4 | 未公開 |

## 四足：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [Quadruped Soccer Shooting](https://arxiv.org/abs/2208.01160) | UC Berkeley / Mila | 階層式 RL：高層規劃踢球軌跡、低層追蹤，四足實機精準把球踢向指定目標 | IROS 2022 | 90 | 未公開 |
| 新興 | 獲獎 | 2024 | [Confined-Space Legged Locomotion](https://arxiv.org/abs/2403.00187) | ETH RSL | 以 3D 體素表示輸入 RL 策略，四足能調整姿態鑽過狹窄空間 | ICRA 2024 | 68 | 未公開 |
| 新興 | 獲獎 | 2023 | [Resilient Legged Local Navigation](https://arxiv.org/abs/2310.03581) | ETH RSL | 把感知失效建模成看不見的障礙與坑洞，RL 局部導航策略學會靠本體感覺應變 | ICRA 2024 | 51 | 未公開 |
| 新興 | 獲獎 | 2023 | [Multi-IMU Proprioceptive Odometry](https://doi.org/10.1109/IROS55552.2023.10342061) | CMU | 在每條小腿加裝 IMU，以 EKF 融合做低漂移的腿式本體感覺里程計 | IROS 2023 | 41 | [82](https://github.com/ShuoYangRobotics/Multi-IMU-Proprioceptive-Odometry) |
| 新興 | 獲獎 | 2022 | [Distributed DDPC Collaborative Legged](https://arxiv.org/abs/2211.06917) | Virginia Tech / Caltech | 以行為系統理論建模多台互相拘束的四足，分散式資料驅動預測控制協同行走 | ICRA 2023 | 33 | 未公開 |
| 新興 | 獲獎 | 2024 | [Quadruped Ladder Climbing](https://arxiv.org/abs/2409.17731) · [專案頁](https://sites.google.com/leggedrobotics.com/climbingladders) | ETH RSL | 特製鉤爪加上 RL 策略，四足實機可靠爬工業爬梯 | IROS 2025 | 26 | 未公開 |
| 新興 | 獲獎 | 2022 | [PI-ARS](https://arxiv.org/abs/2207.13224) · [專案頁](https://kuanghuei.github.io/piars) | Google Research | 以預測資訊表示壓縮視覺輸入，讓演化策略能訓練較大的視覺步行策略 | IROS 2022 | 21 | 未公開 |
| 新興 | 獲獎 | 2023 | [Steep Planetary Terrain Locomotion](https://doi.org/10.1109/IROS55552.2023.10341665) | ETH Zurich | 針對行星陡坡與鬆軟地形的四足行走策略 | IROS 2023 | 21 | 未公開 |
| 新興 | 獲獎 | 2024 | [Leader Following Quadruped](https://arxiv.org/abs/2410.00572) | ETH RSL | 四足以視覺追蹤領隊者並同時避障，免手動遙控跟隨 | ICRA 2025 | 18 | 未公開 |
| 新興 | 獲獎 | 2022 | [Motion Primitive Graph](https://arxiv.org/abs/2209.07503) | Caltech | 在動作基元圖上規劃，依擾動即時切換步態基元，提升腿式機器人穩健性 | ICRA 2023 | 16 | 未公開 |
| 新興 | 獲獎 | 2021 | [Mini Cheetah Optimal Landing](https://arxiv.org/abs/2110.02799) | MIT / UMass Amherst | 不預設接觸序列，即時最佳化落地姿勢與反作用力，從各種墜落狀態恢復 | ICRA 2022 | 8 | 未公開 |

## 輪足（雙足輪、四足輪）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [Track-leg / Wheel-leg TrajOpt](https://doi.org/10.1109/ICRA46639.2022.9812199) | Florida State | 具平滑解析導數的軌跡最佳化，讓履帶腿、輪腿機器人規劃翻越大型障礙 | ICRA 2022 | 4 | 未公開 |

## SLAM 與定位：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [EDPLVO](https://doi.org/10.1109/ICRA46639.2022.9812133) | Meituan / UNC / CMU | 把共線約束有效納入直接法，點線並用的高效直接視覺里程計 | ICRA 2022 | 40 | 未公開 |
| 新興 | 獲獎 | 2023 | [NGEL-SLAM](https://arxiv.org/abs/2311.09525) | Zhejiang | 特徵式追蹤加回環確保全域一致，多個神經隱式子地圖做低延遲稠密建圖 | ICRA 2024 | 39 | [69](https://github.com/YunxuanMao/NGEL_SLAM) |
| 新興 | 獲獎 | 2021 | [Ground Encoding](https://arxiv.org/abs/2103.15317) | CMU | 把透地雷達訊號學成因子圖量測模型，不需事前地圖或 GPS 就能定位 | IROS 2021 | 20 | 未公開 |
| 新興 | 獲獎 | 2023 | [MESA](https://arxiv.org/abs/2310.12320) | CMU | 在流形上的共識 ADMM 後端，多機器人非同步分散式最佳化 SLAM | ICRA 2024 | 20 | 未公開 |
| 新興 | 獲獎 | 2023 | [Semantic Object Map Localization](https://arxiv.org/abs/2303.04658) | MIT | 以物件語意地圖做跨視角配準，不依賴道路特徵，在非都市環境做全域定位與重定位 | IROS 2023 | 16 | 未公開 |
| 新興 | 獲獎 | 2022 | [Data-driven Event Feature Tracking](https://arxiv.org/abs/2211.12826) | UZH RPG | 第一個資料驅動的事件相機特徵追蹤器，有無影像幀都能用，自監督適應真實資料 | CVPR 2023、TPAMI 2025 | 16 | 未公開 |
| 新興 | 獲獎 | 2021 | [Unsupervised LiDAR Features](https://arxiv.org/abs/2102.11261) | University of Toronto | 在高斯變分推論框架內非監督學習 LiDAR 特徵，與軌跡估計共用單一目標 | RA-L 2021 | 16 | 未公開 |
| 新興 | 獲獎 | 2023 | [iMODE](https://doi.org/10.1109/ICRA48891.2023.10161538) | Imperial | 以稀疏 SLAM 位姿與深度監督，即時從頭訓練單目稠密語意神經場 | ICRA 2023 | 16 | 未公開 |
| 新興 | 獲獎 | 2024 | [Censible](https://doi.org/10.1109/ICRA57147.2024.10611697) | Caltech / JPL | 行星車全域定位框架，取代人工比對軌道影像 | ICRA 2024 | 13 | 未公開 |
| 新興 | 獲獎 | 2021 | [Interval-Based Visual-LiDAR Fusion](https://doi.org/10.1109/LRA.2021.3057572) | Leibniz University Hannover | 以區間分析保守建模 LiDAR 距離指派給影像特徵的不確定性 | RA-L 2021 | 12 | 未公開 |
| 新興 | 獲獎 | 2023 | [Cross-View Place Recognition](https://doi.org/10.1109/IROS55552.2023.10341898) | University of Maryland | 保留視覺、空間、幾何資訊的語意地點辨識，用於空地協同的跨視角跨模態定位 | IROS 2023 | 10 | 未公開 |
| 新興 | 獲獎 | 2024 | [Square-Root Filter VINS](https://doi.org/10.1109/ICRA57147.2024.10610916) | University of Delaware | 改用平方根共變異數濾波，在嵌入式裝置上更快且數值更穩 | ICRA 2024 | 10 | 未公開 |
| 新興 | 獲獎 | 2023 | [GMCR](https://arxiv.org/abs/2303.04032) | TUM / Glasgow / Radboud | 以圖式最大共識估計做點雲配準，在高離群比例下仍穩健 | ICRA 2023 | 6 | 未公開 |

## SLAM 與定位：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用 | 2021 | [PointDSC](https://arxiv.org/abs/2103.05465) | HKUST / CityU | 把空間一致性做成可學習的離群點剔除，提升特徵式點雲配準的穩健度 | CVPR 2021 | 399 | [274](https://github.com/XuyangBai/PointDSC) |
| 主流 | 引用 | 2021 | [CoFiNet](https://arxiv.org/abs/2110.14076) | NUDT / TUM / Siemens | 由粗到細的對應：先在超點層級匹配再細化到點，不依賴重複性關鍵點 | NeurIPS 2021 | 376 | [138](https://github.com/haoyu94/Coarse-to-fine-correspondences) |
| 主流 | 引用、獲獎 | 2022 | [Active SLAM Survey](https://arxiv.org/abs/2207.00254) | Zaragoza / MIT SPARK / UCSD 等 | 主動 SLAM 與多機器人協作探索的綜述 | T-RO 2023 | 367 | 未公開 |
| 主流 | 引用、獲獎、機構 | 2021 | [Scan Context++](https://arxiv.org/abs/2109.13494) | KAIST / NAVER LABS / SNU | 對旋轉與橫向位移穩健的 LiDAR 結構地點描述子 | T-RO 2022 | 358 | [347](https://github.com/gisbi-kim/scancontext_tro) |
| 主流 | 引用、獲獎 | 2021 | [Kimera-Multi](https://arxiv.org/abs/2106.14386) | MIT SPARK | 多機器人分散式度量-語意 SLAM | T-RO 2022 | 350 | [417](https://github.com/MIT-SPARK/Kimera-Multi) |
| 主流 | 引用 | 2022 | [REGTR](https://arxiv.org/abs/2203.14517) | NUS | 用 transformer 直接輸出對應點，免最近鄰匹配與 RANSAC，端到端點雲配準 | CVPR 2022 | 315 | [273](https://github.com/yewzijian/RegTR) |
| 主流 | 引用 | 2022 | [ESLAM](https://arxiv.org/abs/2211.11704) · [專案頁](https://www.idiap.ch/paper/eslam/) | Idiap / EPFL / ams OSRAM | 多尺度軸對齊特徵平面表示 SDF 的高效稠密 SLAM | CVPR 2023 | 306 | [224](https://github.com/idiap/ESLAM) |
| 主流 | 引用 | 2023 | [EigenPlaces](https://arxiv.org/abs/2308.10832) | PoliTo | 依主成分方向分群取多視角訓練的視角穩健 VPR | ICCV 2023 | 181 | [163](https://github.com/gmberton/EigenPlaces) |
| 主流 | 引用 | 2023 | [R2Former](https://arxiv.org/abs/2304.03410) | ByteDance / UCF | 單一 Transformer 統一檢索與重排序的地點辨識 | CVPR 2023 | 171 | [104](https://github.com/bytedance/R2Former) |
| 主流 | 引用 | 2023 | [LiDAR Odometry Survey](https://arxiv.org/abs/2312.17487) | SNU | 依感測器融合方式分類的 LiDAR 里程計綜述 | Intelligent Service Robotics 2024 | 152 | 未公開 |
| 主流 | 引用 | 2024 | [CricaVPR](https://arxiv.org/abs/2402.19231) | Tsinghua / Peng Cheng Lab / UCAS | 批次內跨影像注意力學習相關性感知的 VPR 表示 | CVPR 2024 | 116 | [173](https://github.com/Lu-Feng/CricaVPR) |
| 主流 | 引用 | 2024 | [LoopSplat](https://arxiv.org/abs/2408.10154) · [專案頁](https://loopsplat.github.io/) | Stanford / Univ. of Amsterdam / ETH | 直接配準 3DGS 子地圖做迴環的 Gaussian SLAM | 3DV 2025 | 107 | [400](https://github.com/GradientSpaces/LoopSplat) |
| 主流 | 引用 | 2024 | [BoQ](https://arxiv.org/abs/2405.07364) | Laval | 以一組可學習全域查詢聚合特徵的單階段 VPR | CVPR 2024 | 106 | [195](https://github.com/amaralibey/bag-of-queries) |
| 主流 | 引用 | 2024 | [CG-SLAM](https://arxiv.org/abs/2403.16095) · [專案頁](https://zju3dv.github.io/cg-slam) | Zhejiang | 不確定度感知且幾何一致的 Gaussian 場 RGB-D SLAM | ECCV 2024 | 104 | [125](https://github.com/hjr37/CG-SLAM) |
| 主流 | 引用 | 2024 | [SelaVPR](https://arxiv.org/abs/2402.14505) | Tsinghua / Peng Cheng Lab / UCAS | 以輕量 adapter 做全域與局部調適的基礎模型 VPR | ICLR 2024 | 101 | [269](https://github.com/Lu-Feng/SelaVPR) |
| 主流 | 引用、獲獎 | 2024 | [BTC](https://doi.org/10.1109/TRO.2024.3353076) | HKU MaRS | 二值 + 三角形組合描述子的 3D LiDAR 地點辨識 | T-RO 2024 | 84 | [373](https://github.com/hku-mars/btc_descriptor) |
| 主流 | 引用 | 2024 | [LIV-GaussMap](https://arxiv.org/abs/2401.14857) | HKUST / HKUST (GZ) 等 | LiDAR 慣性視覺融合的即時 Gaussian 輻射場建圖 | RA-L 2024 | 81 | [160](https://github.com/sheng00125/LIV-GaussMap) |
| 主流 | 引用 | 2025 | [S3PO-GS](https://arxiv.org/abs/2507.03737) · [專案頁](https://3dagentworld.github.io/S3PO-GS/) | HKUST (GZ) | 以 3DGS 點圖錨定追蹤避免尺度漂移的戶外單目 SLAM | ICCV 2025 | 36 | [138](https://github.com/3DAgentWorld/S3PO-GS) |
| 主流 | 引用 | 2025 | [Adaptive-LIO](https://arxiv.org/abs/2503.05077) | 未確認 | 依環境自適應分段與地圖解析度的 LiDAR 慣性里程計 | IoT-J 2025 | 36 | [272](https://github.com/chengwei0427/Adaptive-LIO) |
| 主流 | 引用 | 2025 | [Ground-Fusion++](https://arxiv.org/abs/2507.08364) | Chongqing / Nankai / ZJUT 等 | GNSS、RGB-D、LiDAR、IMU、輪速的模組化融合 | IROS 2025 | 34 | [228](https://github.com/sjtuyinjie/Ground-Fusion2) |
| 主流 | 引用、Star、獲獎、機構 | 2025 | [GS-LIVO](https://arxiv.org/abs/2501.08672) | HKUST / HKU MaRS / SJTU | 可在嵌入式即時運行的 LiDAR 慣性視覺 Gaussian 建圖 | T-RO 2025 | 32 | [505](https://github.com/HKUST-Aerial-Robotics/GS-LIVO) |
| 主流 | 引用 | 2025 | [OpenGS-SLAM (outdoor)](https://arxiv.org/abs/2502.15633) · [專案頁](https://3dagentworld.github.io/opengs-slam/) | HKUST (GZ) | 點圖回歸加自適應尺度的戶外純 RGB Gaussian SLAM | ICRA 2025 | 32 | [215](https://github.com/3DAgentWorld/OpenGS-SLAM) |
| 主流 | 引用、獲獎 | 2025 | [VINGS-Mono](https://arxiv.org/abs/2501.08286) · [專案頁](https://vings-mono.github.io/) | Fudan | 視覺慣性單目 Gaussian SLAM 擴展到公里級戶外 | T-RO 2025 | 31 | [306](https://github.com/Fudan-MAGIC-Lab/VINGS-Mono) |
| 主流 | 引用、獲獎 | 2025 | [OKVIS2-X](https://arxiv.org/abs/2510.04612) | TUM | 可選配稠密深度、LiDAR 與 GNSS 的關鍵幀 VI-SLAM | T-RO 2025 | 31 | [421](https://github.com/ethz-mrl/OKVIS2-X) |
| 新興 | 獲獎 | 2022 | [Localizability Estimation](https://arxiv.org/abs/2203.05698) | ETH RSL | 從點雲直接學習各方向的可定位性，隧道等退化場景提前偵測並調整 LiDAR 定位 | IROS 2022 | 53 | [101](https://github.com/leggedrobotics/L3E) |
| 新興 | 獲獎 | 2025 | [Back on Track](https://arxiv.org/abs/2504.14516) · [專案頁](https://wrchen530.github.io/projects/batrack/) | TUM / Oxford / Microsoft | 用 3D 點追蹤把動態點的運動拆成相機與物體分量，讓 BA 能直接處理動態影片 | ICCV 2025 | 26 | [105](https://github.com/wrchen530/batrack) |
| 新興 | 獲獎 | 2025 | [Ground-Optimized 4D Radar-Inertial Odometry](https://arxiv.org/abs/2502.08093) | SNU | 地面最佳化的雜訊濾除，加上以高斯過程連續積分速度的雷達慣性里程計 | ICRA 2025 | 13 | [109](https://github.com/wooseongY/Go-RIO) |
| 新興 | 獲獎 | 2025 | [Doppler Correspondence](https://arxiv.org/abs/2502.11461) | UNIST / KAIST | 用 4D LiDAR／雷達的 Doppler 速度直接建立對應，掃描匹配不需迭代，在隧道、惡劣天氣更穩 | RSS 2025 | 6 | [46](https://github.com/Tars0523/Doppler_Correspondence) |
| 新興 | 獲獎 | 2025 | [FUSER](https://arxiv.org/abs/2512.09373) | NTU / Nanjing / Nankai / Alibaba | 一次處理所有掃描直接回歸全域位姿，免成對匹配，再以 SE(3)^N diffusion 精修 | CVPR 2026 | 6 | 未公開 |

## 3D 場景重建（feed-forward、SfM、3DGS／NeRF）：超過主題上限

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用 | 2025 | [SuperPC](https://arxiv.org/abs/2503.14558) | University at Buffalo | 單一 diffusion 模型同時處理點雲補全、上採樣、去噪與上色，避免各任務串接誤差 | CVPR 2025 | 30 | [25](https://github.com/sair-lab/SuperPC) |
| 新興 | 獲獎 | 2021 | [Learning to Solve Hard Minimal Problems](https://arxiv.org/abs/2112.03424) | Georgia Tech / CTU Prague | 學習挑選起始問題解對做同倫延拓，只算出需要的那個解，大幅加速難的最小問題求解 | CVPR 2022 | 42 | [146](https://github.com/petrhruby97/learning_minimal) |
| 新興 | 獲獎 | 2025 | [FastMap](https://arxiv.org/abs/2505.04612) · [專案頁](https://jiahao.ai/fastmap) | TTIC / Toyota Research Institute | 只用一階最佳化的全域 SfM，GPU 上比 COLMAP、GLOMAP 快約 10 倍、位姿精度相當 | 3DV 2026 | 7 | [292](https://github.com/pals-ttic/fastmap) |
| 新興 | 獲獎 | 2025 | [Anisotropic Rotation Averaging](https://arxiv.org/abs/2503.07353) | Lund / Chalmers | 把量測的各向異性不確定性放進旋轉平均，並給出可驗證全域最優的鬆弛解 | ICCV 2025 | 3 | [11](https://github.com/ylochman/anisotropic-ra) |

## 深度估計與 occupancy：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2021 | [Binary TTC](https://arxiv.org/abs/2101.04777) | NVIDIA / UCSB | 把碰撞時間估計改成逐像素二元分類（是否在時限內碰撞），單目、免校正即可當時間柵欄 | CVPR 2021 | 40 | 未公開 |
| 新興 | 獲獎 | 2021 | [Neural Disparity Refinement](https://arxiv.org/abs/2110.15367) · [專案頁](https://cvlab-unibo.github.io/neural-disparity-refinement-web) | Bologna | 連續式視差精修網路，可輸出任意解析度，適合手機上高低解析度不對稱的雙目 | 3DV 2021 | 34 | [63](https://github.com/CVLAB-Unibo/neural-disparity-refinement) |

## 3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [InterObject3D](https://arxiv.org/abs/2204.07183) | ETH / RWTH Aachen | 使用者點擊迭代修正的互動式 3D 實例分割，可泛化到訓練外類別 | ICRA 2023 | 35 | [42](https://github.com/theodorakontogianni/InterObject3D) |
| 新興 | 獲獎 | 2021 | [Category-level Pose and Shape](https://arxiv.org/abs/2104.08383) | MIT | 給類別 CAD 庫的主動形狀模型，以可驗證全域最優的凸鬆弛同時解物件位姿與形狀，對離群點穩健 | RSS 2021 | 29 | 未公開 |
| 新興 | 獲獎 | 2024 | [HEGN](https://doi.org/10.1109/ICRA57147.2024.10610562) | Siemens / TUM | 階層式等變圖網路做含縮放的 9DoF 點雲配準，用於類別級位姿估計 | ICRA 2024 | 1 | 未公開 |

## 電腦視覺（偵測、分割、視覺基礎模型）：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2024 | [Evidential OOD Segmentation](https://doi.org/10.1109/ICRA57147.2024.10611342) | MIT / ARL | 不需 OOD 樣本，以證據式深度學習估計語意分割的逐像素不確定性，偵測未知障礙 | ICRA 2024 | 26 | 未公開 |

## 模擬與 Real2Sim：新興滿兩年未達門檻

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 新興 | 獲獎 | 2022 | [NeRF2Real](https://arxiv.org/abs/2210.04932) · [專案頁](https://sites.google.com/view/nerf2real/home) | DeepMind | 手機影片建 NeRF 取得接觸幾何與新視角渲染，在模擬中訓練視覺策略後轉移到實機 | ICRA 2023 | 80 | 未公開 |

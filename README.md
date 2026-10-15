# Robot Nav Survey

AMR、四足、輪足機器人的導航、視覺、3D 感知、SLAM 與 Real2Sim 前沿論文整理，每三天自動更新。

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 或 digests/ 後重跑 -->

- 每三天由排程 agent 依 [CLAUDE.md](CLAUDE.md) 的規則搜尋新論文並開 PR，審過再 merge。
- 手動更新：在 repo 裡開 Claude Code，說「更新論文整理」。
- 每個主題分三段：在解決的問題、經典（近五年，依引用與 star 分級）、最新論文。
- 分級：**奠基** 引用 ≥ 1000 或 star ≥ 10k；**主流** 引用 ≥ 300 或 star ≥ 1k；其餘為**新興**。引用來自 Semantic Scholar，star 來自 GitHub。「年」是 arXiv 首次公開年份，「來源」是正式刊登的會議或期刊。
- 程式碼標「未公開」：論文頁、arXiv 頁與 GitHub 搜尋都找不到作者釋出的官方程式碼（第三方重現不算）。

## 定期追蹤的來源

完整查法與關鍵字見 [CLAUDE.md](CLAUDE.md#搜尋方式)。

- **NVIDIA Research**（每次必查）：[Robotics](https://research.nvidia.com/research-area/robotics)、[Computer Vision](https://research.nvidia.com/research-area/computer-vision)、[Seattle Robotics Lab](https://research.nvidia.com/labs/srl)、[GEAR](https://research.nvidia.com/labs/gear/)、[NVlabs GitHub](https://github.com/NVlabs)
- **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics
- **實驗室**：[ETH RSL](https://rsl.ethz.ch)、[ETH ASL](https://asl.ethz.ch)、[MIT SPARK](https://web.mit.edu/sparklab/)、[CMU AirLab](https://theairlab.org)、[Berkeley RAIL](https://rail.eecs.berkeley.edu)、[UCSD Xiaolong Wang](https://xiaolonw.github.io)、[PKU EPIC](https://pku-epic.github.io)、[InternRobotics](https://github.com/InternRobotics)、[Oxford VGG](https://www.robots.ox.ac.uk/~vgg/)、[Oxford DRS](https://dynamic.robots.ox.ac.uk)、[Freiburg](https://rl.uni-freiburg.de)、[TUM CVG](https://cvg.cit.tum.de)、[HKU MaRS](https://mars.hku.hk)、[ZJU FAST Lab](https://github.com/ZJU-FAST-Lab)、[KAIST RaiLab](https://railab.kaist.ac.kr)
- **arXiv**：cs.RO、cs.CV，依主題關鍵字查上次更新後的新投稿
- **期刊**：Science Robotics、RA-L、T-RO
- **會議**：CoRL、RSS、ICRA、IROS、CVPR（接收論文公布時）

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

### 在解決的問題

- 語言對應到空間：把「走到廚房冰箱旁」對到畫面與地圖上的位置。
- 長程、部分可觀測：指令長、環境沒看過，需要記憶與探索。
- sim-to-real：benchmark 多在 Habitat 模擬，實機成功率落差大。
- 推論延遲：數 B 參數的 VLM 難以機上即時跑，近期多改成「慢 VLM 推理 + 快控制層」。
- 跨機體：同一模型用在輪式、四足、人形。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 主流 | 2022 | [LM-Nav](https://arxiv.org/abs/2207.04429) · [專案頁](https://sites.google.com/view/lmnav) | UC Berkeley | 用現成 LLM + VLM + ViNT 類導航模型組合，不需標註語言資料就能照指令走 | CoRL 2022 | 824 | [272](https://github.com/blazejosinski/lm_nav) |
| 主流 | 2023 | [NavGPT](https://arxiv.org/abs/2305.16986) | Adelaide / ANU | 純 LLM 推理做 VLN，把觀測轉文字 | AAAI 2024 | 498 | [352](https://github.com/GengzeZhou/NavGPT) |
| 主流 | 2023 | [VLFM](https://arxiv.org/abs/2312.03275) · [專案頁](http://naoki.io/vlfm) | Boston Dynamics AI Institute | VLM 算語意價值地圖引導 frontier 探索，Spot 實機 zero-shot 物件導航 | ICRA 2024 | 450 | [821](https://github.com/bdaiinstitute/vlfm) |
| 主流 | 2022 | [CoW (CLIP on Wheels)](https://arxiv.org/abs/2203.10421) · [專案頁](https://cow.cs.columbia.edu/) | Columbia | 把 CLIP 接上探索策略做 zero-shot 物件導航 | CVPR 2023 | 362 | [158](https://github.com/real-stanford/cow) |
| 主流 | 2024 | [NaVid](https://arxiv.org/abs/2402.15852) · [專案頁](https://pku-epic.github.io/NaVid/) | PKU | 只用單眼 RGB 影片的 VLM 做 VLN，不需地圖與深度 | RSS 2024 | 342 | [455](https://github.com/jzhzhang/NaVid-VLN-CE) |
| 主流 | 2024 | [NaVILA](https://arxiv.org/abs/2412.04453) · [專案頁](https://navila-bot.github.io/) | UCSD / NVIDIA | VLM 輸出中層語言動作，低層腿式運動策略執行 | RSS 2025 | 333 | [721](https://github.com/AnjieCheng/NaVILA) |
| 新興 | 2023 | [ETPNav](https://arxiv.org/abs/2304.03047) | UCAS / CASIA 等 | 連續環境 VLN 用線上拓撲圖做高層規劃 | TPAMI 2024 | 296 | [496](https://github.com/MarSaKi/ETPNav) |
| 新興 | 2024 | [Uni-NaVid](https://arxiv.org/abs/2412.06224) · [專案頁](https://pku-epic.github.io/Uni-NaVid/) | PKU | 一個 VLM 統一 VLN、物件導航、問答、跟人等導航任務 | RSS 2025 | 228 | [358](https://github.com/jzhzhang/Uni-NaVid) |
| 新興 | 2024 | [Mobility VLA](https://arxiv.org/abs/2407.07775) | Google DeepMind | 長脈絡 VLM 看導覽影片建拓撲圖，再照多模態指令導航 | CoRL 2024 | 102 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | [Robostral Navigate](https://arxiv.org/abs/2607.20785) · [專案頁](https://mistral.ai/news/robostral-navigate) | Mistral AI | 8B VLM 只用單眼 RGB，在畫面上指出下一個目標點；目標不在視野時輸出局部座標位移 | R2R-CE val-unseen SR 76.6%；online RL +3.2% | 未公開 | arXiv、Mistral 官網 |
| 2026-07 | [ABot-N1](https://arxiv.org/abs/2607.10383) · [專案頁](https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/) | Alibaba AMAP | 慢 VLM 推理出影像錨點，快模組轉成連續 waypoint；同一架構做 point/object/POI/指令/跟人五種任務 | 室內 95.4%、室外 92.9% SR；POI 抵達 77.3% | [GitHub](https://github.com/amap-cvlab/ABot-Navigation) | arXiv |
| 2026-07 | [GemNav](https://arxiv.org/abs/2607.06882) | CSIRO | MLLM 輸出離散 token 當導航動作 |  | 未公開 | arXiv |
| 2026-04 | [Robot Navigation via Foundation Language Models: A Review](https://dl.acm.org/doi/10.1145/3802539) | ECNU / HIT 等 | ACM CSUR 綜述 |  | 未公開 | ACM Computing Surveys 2026 |

## 局部導航策略（diffusion / world model）

### 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 主流 | 2023 | [NoMaD](https://arxiv.org/abs/2310.07896) · [專案頁](https://general-navigation-models.github.io/nomad/) | UC Berkeley | diffusion policy 統一有目標導航與無目標探索 | ICRA 2024 | 450 | [1,326](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 2023 | [ViNT](https://arxiv.org/abs/2306.14846) · [專案頁](https://visualnav-transformer.github.io) | UC Berkeley | 導航基礎模型：Transformer + 影像目標，可微調到新任務 | CoRL 2023 | 416 | [1,326](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 2024 | [Navigation World Models](https://arxiv.org/abs/2412.03572) · [專案頁](https://www.amirbar.net/nwm/) | Meta | 可控影片生成的導航 world model，用想像軌跡做規劃 | CVPR 2025 | 363 | [698](https://github.com/facebookresearch/nwm) |
| 主流 | 2022 | [GNM](https://arxiv.org/abs/2210.03370) · [專案頁](https://sites.google.com/view/drive-any-robot) | UC Berkeley | 跨多種機器人資料訓練的通用視覺導航模型 | ICRA 2023 | 311 | [1,326](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 2021 | [FAR Planner](https://arxiv.org/abs/2110.09460) | CMU | 未知環境中邊建可視圖邊規劃的快速路徑規劃 | IROS 2022 | 90 | [1,024](https://github.com/MichaelFYang/far_planner) |
| 新興 | 2023 | [ViPlanner](https://arxiv.org/abs/2310.00982) | ETH | 加入語意的可微分局部規劃，腿式機器人實機 | ICRA 2024 | 111 | [677](https://github.com/leggedrobotics/viplanner) |
| 新興 | 2023 | [iPlanner](https://arxiv.org/abs/2302.11434) | CMU / ETH | 自監督學習的端到端局部規劃，以可微分代價取代標註 | RSS 2023 | 97 | [370](https://github.com/leggedrobotics/iPlanner) |
| 新興 | 2025 | [NavDP](https://arxiv.org/abs/2505.08712) · [專案頁](https://wzcai99.github.io/navigation-diffusion-policy.github.io) | Shanghai AI Lab | 純模擬訓練 diffusion 導航策略 + 特權資訊引導，zero-shot sim-to-real | ICRA 2026 | 87 | [811](https://github.com/InternRobotics/NavDP) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 未公開 | arXiv |
| 2026-08 | [UniNav](https://arxiv.org/abs/2608.03244) | HKUST (GZ) / CUHK-SZ | 統一 world-action diffusion |  | 未公開 | arXiv |
| 2026-08 | [ODG-NoMaD](https://arxiv.org/abs/2608.21395) | 論文未標示 | NoMaD 加俯視相機方向引導 |  | 未公開 | arXiv |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) · [專案頁](https://yty-sky.github.io/x-navdp-project-page) | Shanghai AI Lab / Fudan / SYSU | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） |  | 未公開 | arXiv |
| 2026-06 | [NavWM](https://arxiv.org/abs/2606.24101) | CASIA / Beihang | 導航 world model 做前瞻規劃 |  | 未公開 | arXiv |
| 2026-06 | [NavWAM](https://arxiv.org/abs/2606.13494) · [專案頁](https://dachii-azm.github.io/navwam/) | Univ. of Tokyo | goal-conditioned world action model |  | 未公開 | arXiv |
| 2026-05 | [NavOL](https://arxiv.org/abs/2605.11762) · [專案頁](https://logosroboticsgroup.github.io/NavOL/) | Fudan / Shanghai Innovation Institute | diffusion 導航策略在 IsaacLab 線上模仿學習，解 NavDP 離線資料限制 |  | [GitHub](https://github.com/WAboutMe/NavOL) | arXiv |
| 2026-03 | [Beyond Imitation](https://arxiv.org/abs/2603.12868) | NTU / A*STAR / NUS | RL 微調 diffusion 導航策略 |  | 未公開 | arXiv |

## 語意地圖與場景圖

### 在解決的問題

- 開放詞彙：不限定類別，能用任意語言查物件與區域。
- 可擴展：稠密特徵地圖太大，改用物件／房間／樓層的階層場景圖壓縮。
- 即時、增量：邊走邊建，並處理場景變動。
- 當成 LLM／VLM 規劃的介面。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 主流 | 2022 | [OpenScene](https://arxiv.org/abs/2211.15654) · [專案頁](https://pengsongyou.github.io/openscene) | ETH / Google | 零樣本開放詞彙 3D 場景理解 | CVPR 2023 | 806 | [853](https://github.com/pengsongyou/openscene) |
| 主流 | 2023 | [LERF](https://arxiv.org/abs/2303.09553) · [專案頁](https://lerf.io) | UC Berkeley | 把 CLIP 特徵嵌進 NeRF 做語言查詢 | ICCV 2023 | 767 | [734](https://github.com/kerrj/lerf) |
| 主流 | 2022 | [VLMaps](https://arxiv.org/abs/2210.05714) · [專案頁](https://vlmaps.github.io) | Freiburg / Google | 把 VLM 特徵融合進 3D 地圖，可用語言查空間位置 | ICRA 2023 | 708 | [729](https://github.com/vlmaps/vlmaps) |
| 主流 | 2023 | [ConceptGraphs](https://arxiv.org/abs/2309.16650) · [專案頁](https://concept-graphs.github.io/) | Toronto / MIT | 用 2D 基礎模型建開放詞彙 3D 場景圖，支援 LLM 規劃 | ICRA 2024 | 673 | [971](https://github.com/concept-graphs/concept-graphs) |
| 主流 | 2023 | [ConceptFusion](https://arxiv.org/abs/2302.07241) · [專案頁](https://concept-fusion.github.io) | MIT / Toronto | 把基礎模型特徵融合成開放集合 3D 地圖 | RSS 2023 | 454 | [246](https://github.com/concept-fusion/concept-fusion) |
| 主流 | 2022 | [Hydra](https://arxiv.org/abs/2201.13360) | MIT SPARK | 即時建立階層式 3D 場景圖（物件／房間／樓層） | RSS 2022 | 393 | [1,180](https://github.com/MIT-SPARK/Hydra) |
| 主流 | 2024 | [HOV-SG](https://arxiv.org/abs/2403.17846) · [專案頁](http://hovsg.github.io/) | Freiburg | 樓層／房間／物件階層開放詞彙場景圖，跨樓層語言導航 | RSS 2024 | 355 | [555](https://github.com/hovsg/HOV-SG) |
| 新興 | 2024 | [Clio](https://arxiv.org/abs/2404.13696) | MIT SPARK | 依任務決定物件粒度的場景圖（information bottleneck） | RA-L 2024 | 155 | [263](https://github.com/MIT-SPARK/Clio) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05 | [LEXI-SG](https://arxiv.org/abs/2605.13741) · [專案頁](https://ori-drs.github.io/lexisg-web/) | Oxford | 只用單眼 RGB 建開放詞彙 3D 場景圖，以房間為單位 feed-forward 重建 | 評估在 HM3D 與自錄辦公室序列，未做實機導航 | 未公開 | RA-L 2026 |
| 2026-03 | [OGScene3D](https://arxiv.org/abs/2603.16301) | SJTU / UTN / Cambridge / NTU | 邊探索邊增量建場景圖，confidence-aware Gaussian 語意表示 |  | [GitHub](https://github.com/IRMVLab/OGScene3D) | arXiv |

## 四足

### 在解決的問題

- 感知不可靠時仍要穩（反光、草叢、高度圖雜訊）：融合外部感知與本體感知。
- sim-to-real：大規模平行模擬 + domain randomization + 特權教師蒸餾。
- 敏捷技能（跑酷、跳躍、越溝）與技能切換。
- 從「跟隨速度指令」走向「運動與導航一體」，直接走到目標。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 奠基 | 2022 | [Perceptive Locomotion in the Wild](https://arxiv.org/abs/2201.08117) | ETH | 高度圖感知 + 本體感知的注意力融合，ANYmal 野外實機 | Science Robotics 2022 | 1,259 | 未公開 |
| 奠基 | 2021 | [Learning to Walk in Minutes](https://arxiv.org/abs/2109.11978) · [專案頁](https://leggedrobotics.github.io/legged_gym/) | ETH | GPU 大規模平行 RL，幾分鐘訓練出運動策略（legged_gym） | CoRL 2021 | 1,178 | [3,145](https://github.com/leggedrobotics/legged_gym) |
| 奠基 | 2021 | [RMA](https://arxiv.org/abs/2107.04034) · [專案頁](https://ashish-kmr.github.io/rma-legged-robots/) | UC Berkeley / CMU | 快速自適應模組：以本體感知線上估計環境參數 | RSS 2021 | 1,122 | 未公開 |
| 主流 | 2023 | [ANYmal Parkour](https://arxiv.org/abs/2306.14874) · [專案頁](https://sites.google.com/leggedrobotics.com/agile-navigation) | ETH | 感知、移動、技能選擇分模組的跑酷導航 | Science Robotics 2024 | 485 | 未公開 |
| 主流 | 2023 | [Extreme Parkour](https://arxiv.org/abs/2309.14341) · [專案頁](https://extreme-parkour.github.io/) | CMU | 單一神經網路以深度相機做極限跑酷 | ICRA 2024 | 423 | [1,186](https://github.com/chengxuxin/extreme-parkour) |
| 主流 | 2022 | [Legged Locomotion with Egocentric Vision](https://arxiv.org/abs/2211.07638) · [專案頁](https://vision-locomotion.github.io) | CMU / Berkeley | 直接用深度影像端到端學運動，不建高度圖 | CoRL 2022 | 367 | 未公開 |
| 主流 | 2023 | [Robot Parkour Learning](https://arxiv.org/abs/2309.05665) · [專案頁](https://robot-parkour.github.io) | Stanford / Shanghai Qi Zhi | 低成本四足以深度相機學跑酷技能 | CoRL 2023 | 346 | [1,134](https://github.com/ZiwenZhuang/parkour) |
| 主流 | 2022 | [Walk These Ways](https://arxiv.org/abs/2212.03238) · [專案頁](https://gmargo11.github.io/walk-these-ways/) | MIT | 多樣行為參數化的單一策略，可調步態 | CoRL 2022 | 345 | [1,464](https://github.com/Improbable-AI/walk-these-ways) |
| 主流 | 2022 | [Elevation Mapping CuPy](https://arxiv.org/abs/2204.12876) | ETH | GPU 加速的機器人中心高度圖，多數感知式運動策略的輸入 | IROS 2022 | 205 | [1,125](https://github.com/leggedrobotics/elevation_mapping_cupy) |
| 新興 | 2023 | [DreamWaQ](https://arxiv.org/abs/2301.10602) · [專案頁](https://sites.google.com/view/dreamwaq) | KAIST | 無外部感知的盲走策略，用隱式地形想像過複雜地形 | ICRA 2023 | 256 | 未公開 |
| 新興 | 2024 | [ABS](https://arxiv.org/abs/2401.17583) · [專案頁](https://agile-but-safe.github.io/) | CMU | 敏捷策略 + 學到的可達避碰價值函數，高速且安全 | RSS 2024 | 183 | [633](https://github.com/LeCAR-Lab/ABS) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | [APT-RL: Agile perceptive multi-skill locomotion](https://arxiv.org/abs/2607.13579) · [專案頁](https://skillquadsr.github.io/) | KAIST 等 | 軌跡最佳化 8 分鐘產生 18 萬條動作先驗，再用 RL + 機載感知適應 3D 地形 | 單一策略過樓梯／欄／踏石／溝；瞬間最高 6 m/s | 未公開 | Science Robotics 2026 |
| 2026-06 | [Perceptive Platform Adaptive Locomotion](https://arxiv.org/abs/2606.25179) | Oxford DRS | 感知只給 critic，感知有雜訊時比完全感知策略穩 |  | 未公開 | arXiv |
| 2026-06 | [GUIDE](https://arxiv.org/abs/2606.10832) · [專案頁](https://guide-navigation.github.io/) | Zhejiang / TeleAI / Oxford 等 | 端到端腿式導航 |  | 未公開 | arXiv |
| 2026-04 | [HiPAN](https://arxiv.org/abs/2604.26504) · [專案頁](https://sgvr.kaist.ac.kr/~Jeil/project_page_HiPAN/) | KAIST | 非結構 3D 環境的姿態自適應分層導航 |  | 未公開 | RA-L 2026 |

## 輪足（雙足輪、四足輪）

### 在解決的問題

- 混合運動：何時滾、何時走、何時跨越，以及模式切換。
- 高速下的感知延遲：建圖更新跟不上速度（Lee et al. 2024 指出這限制了自主時的速度）。
- 硬體負載：輪驅動改變關節受力（Go2-W 髖關節過熱）。
- 雙足輪的平衡與越障；研究多停在運動控制，經典論文少。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 新興 | 2024 | [Wheeled-Legged Urban Navigation](https://arxiv.org/abs/2405.01792) | ETH | 階層式 RL 導航 + 運動，都市公里級自主任務 | Science Robotics 2024 | 216 | 未公開 |
| 新興 | 2022 | [Multiple Adversarial Motion Priors](https://arxiv.org/abs/2203.14912) | ETH | 多個 AMP 讓輪足機器人學會多種技能（站立、行走、滾動） | ICRA 2023 | 119 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | [Traversal Risk Graph Planning](https://arxiv.org/abs/2608.16433) | ShanghaiTech | 考慮機身的穿越風險圖規劃 |  | [GitHub](https://github.com/ZhiqiaoGuo/RB-TRG) | arXiv |
| 2026-06 | [Go2-W Long-Distance Navigation](https://arxiv.org/abs/2606.21387) | Chiba Tech fuRo | 輪子驅動會讓髖關節過熱，訓練能分散負載的策略 | Tsukuba Challenge 2025 自主約 2.8 km（人行道、公園、樓梯） | 未公開 | arXiv |
| 2026-04 | [Reflexive Obstacle Evasion](https://arxiv.org/abs/2604.23761) · [專案頁](https://aware-ral-2026.github.io/) | Tianjin Univ. / Zhongguancun Academy / NUS | 輪足高動態反射式閃避 |  | 未公開 | arXiv |
| 2026-02 | [Sparse MoE multi-mode locomotion](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1788395/full) | Beijing Institute of Technology | 雙足輪；稀疏 MoE RL，在滾動與越障間自動切換 |  | 未公開 | Frontiers in Robotics and AI 2026 |

## SLAM 與定位

### 在解決的問題

- 退化場景：長廊、隧道、空曠處 LiDAR 或視覺特徵不足。
- 多感測器緊耦合：LiDAR、IMU、相機融合。
- 學習式前端：用 DROID、MASt3R、VGGT 等取代手工特徵，處理無紋理、免校正相機。
- 稠密且寫實的地圖：NeRF／3DGS SLAM。
- 大尺度、長期：回環、地點辨識、多機器人、場景隨時間變化。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 奠基 | 2020 | [ORB-SLAM3](https://arxiv.org/abs/2007.11898) | Zaragoza | 視覺／視覺慣性／多地圖 SLAM 的標準基線 | T-RO 2021 | 4,751 | [9,146](https://github.com/UZ-SLAMLab/ORB_SLAM3) |
| 奠基 | 2021 | [FAST-LIO2](https://arxiv.org/abs/2107.06829) | HKU MaRS | 直接點雲配準 + ikd-tree 的快速 LiDAR 慣性里程計 | T-RO 2022 | 1,892 | [5,276](https://github.com/hku-mars/FAST_LIO) |
| 奠基 | 2021 | [DROID-SLAM](https://arxiv.org/abs/2108.10869) | Princeton | 可微分 BA 的深度學習視覺 SLAM | NeurIPS 2021 | 1,270 | [2,710](https://github.com/princeton-vl/DROID-SLAM) |
| 奠基 | 2021 | [NICE-SLAM](https://arxiv.org/abs/2112.12130) · [專案頁](https://pengsongyou.github.io/nice-slam) | ETH / Zhejiang | 階層式神經隱式表示的稠密 SLAM | CVPR 2022 | 1,149 | [1,598](https://github.com/cvg/nice-slam) |
| 主流 | 2023 | [SplaTAM](https://arxiv.org/abs/2312.02126) · [專案頁](https://spla-tam.github.io/) | CMU | 3D Gaussian Splatting 的 RGB-D SLAM | CVPR 2024 | 749 | [2,209](https://github.com/spla-tam/SplaTAM) |
| 主流 | 2023 | [Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741) · [專案頁](https://rmurai.co.uk/projects/GaussianSplattingSLAM/) | Imperial | 單眼即時 3DGS SLAM | CVPR 2024 | 736 | [2,182](https://github.com/muskie82/MonoGS) |
| 主流 | 2022 | [KISS-ICP](https://arxiv.org/abs/2209.15397) | Bonn | 極簡、免調參的 point-to-point ICP LiDAR 里程計 | RA-L 2023 | 608 | [2,347](https://github.com/PRBonn/kiss-icp) |
| 主流 | 2021 | [R3LIVE](https://arxiv.org/abs/2109.07982) | HKU MaRS | LiDAR-慣性-視覺緊耦合，即時彩色地圖 | ICRA 2022 | 421 | [2,472](https://github.com/hku-mars/r3live) |
| 主流 | 2021 | [Kimera-Multi](https://arxiv.org/abs/2106.14386) | MIT SPARK | 多機器人分散式度量-語意 SLAM | T-RO 2022 | 347 | [417](https://github.com/MIT-SPARK/Kimera-Multi) |
| 主流 | 2022 | [DPVO](https://arxiv.org/abs/2208.04726) | Princeton | 稀疏 patch 的深度視覺里程計，比 DROID 輕量 | NeurIPS 2023 | 327 | [1,135](https://github.com/princeton-vl/DPVO) |
| 主流 | 2024 | [MASt3R-SLAM](https://arxiv.org/abs/2412.12392) · [專案頁](https://edexheim.github.io/mast3r-slam/) | Imperial | 以 MASt3R 3D 重建先驗做即時稠密單眼 SLAM | CVPR 2025 | 327 | [3,215](https://github.com/rmurai0610/MASt3R-SLAM) |
| 主流 | 2023 | [AnyLoc](https://arxiv.org/abs/2308.00688) · [專案頁](https://anyloc.github.io/) | CMU / IIIT | 用基礎模型特徵做通用視覺地點辨識 | RA-L 2024 | 319 | [645](https://github.com/AnyLoc/AnyLoc) |
| 主流 | 2024 | [FAST-LIVO2](https://arxiv.org/abs/2408.14035) | HKU MaRS | LiDAR-慣性-視覺直接法緊耦合里程計 | T-RO 2025 | 278 | [4,753](https://github.com/hku-mars/FAST-LIVO2) |
| 主流 | 2025 | [VGGT-SLAM](https://arxiv.org/abs/2505.12549) | MIT SPARK | 用 VGGT 子地圖 + SL(4) 流形優化的 feed-forward SLAM | NeurIPS 2025 | 183 | [1,157](https://github.com/MIT-SPARK/VGGT-SLAM) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
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

## 3D 感知（深度、feed-forward 重建、occupancy）

### 在解決的問題

- 單眼公制深度：要有絕對尺度，且相機內參常未知。
- feed-forward 重建：不跑 SfM 優化，一次前向得到相機與幾何；挑戰在大規模與串流輸入。
- 雙目深度的零樣本泛化。
- 3D 表示：3DGS 取代 NeRF，可即時渲染。
- occupancy：多源自自駕，提供規劃用的 3D 佔據。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 奠基 | 2023 | [3D Gaussian Splatting](https://arxiv.org/abs/2308.04079) · [專案頁](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | Inria | 即時可微分高斯渲染，取代 NeRF 成為主流 3D 表示 | SIGGRAPH 2023 | 10,901 | [24,208](https://github.com/graphdeco-inria/gaussian-splatting) |
| 奠基 | 2021 | [DPT](https://arxiv.org/abs/2103.13413) | Intel | ViT 做稠密預測，後續單眼深度模型的骨幹設計 | ICCV 2021 | 3,171 | [2,331](https://github.com/isl-org/DPT) |
| 奠基 | 2024 | [Depth Anything V2](https://arxiv.org/abs/2406.09414) · [專案頁](https://depth-anything-v2.github.io) | HKU / TikTok | 以合成資料標註提升細節的深度模型 | NeurIPS 2024 | 2,377 | [8,957](https://github.com/DepthAnything/Depth-Anything-V2) |
| 奠基 | 2024 | [Depth Anything](https://arxiv.org/abs/2401.10891) · [專案頁](https://depth-anything.github.io) | HKU / TikTok | 大規模未標註資料訓練的單眼深度基礎模型 | CVPR 2024 | 2,229 | [8,236](https://github.com/LiheYoung/Depth-Anything) |
| 奠基 | 2023 | [DUSt3R](https://arxiv.org/abs/2312.14132) | Naver Labs | 免相機參數直接回歸 pointmap 的 3D 重建 | CVPR 2024 | 2,026 | [7,342](https://github.com/naver/dust3r) |
| 奠基 | 2025 | [VGGT](https://arxiv.org/abs/2503.11651) · [專案頁](https://vgg-t.github.io/) | Oxford VGG / Meta | 單次前向同時估相機、深度、點圖、追蹤 | CVPR 2025 | 2,006 | [14,512](https://github.com/facebookresearch/vggt) |
| 奠基 | 2024 | [MASt3R](https://arxiv.org/abs/2406.09756) | Naver Labs | DUSt3R 加特徵匹配頭，提升匹配與定位 | ECCV 2024 | 1,253 | [3,130](https://github.com/naver/mast3r) |
| 奠基 | 2023 | [ZoeDepth](https://arxiv.org/abs/2302.12288) | Intel | 相對深度預訓練 + 公制深度頭，零樣本公制深度 | arXiv | 1,060 | [2,838](https://github.com/isl-org/ZoeDepth) |
| 主流 | 2025 | [Depth Anything 3](https://arxiv.org/abs/2511.10647) · [專案頁](https://depth-anything-3.github.io/) | ByteDance Seed | 任意視角數的深度與位姿估計 | arXiv | 812 | [6,488](https://github.com/ByteDance-Seed/Depth-Anything-3) |
| 主流 | 2021 | [RAFT-Stereo](https://arxiv.org/abs/2109.07547) | Princeton | 迭代更新的雙目深度估計 | 3DV 2021 | 753 | [1,132](https://github.com/princeton-vl/RAFT-Stereo) |
| 主流 | 2025 | [CUT3R](https://arxiv.org/abs/2501.12387) · [專案頁](https://cut3r.github.io/) | UC Berkeley / Google | 持續狀態更新的串流 3D 重建 | CVPR 2025 | 639 | [1,506](https://github.com/CUT3R/CUT3R) |
| 主流 | 2024 | [Metric3D v2](https://arxiv.org/abs/2404.15506) · [專案頁](https://JUGGHM.github.io/Metric3Dv2) | HKUST 等 | 零樣本公制深度與法向量 | TPAMI 2024 | 585 | [2,328](https://github.com/YvanYin/Metric3D) |
| 主流 | 2024 | [UniDepth](https://arxiv.org/abs/2403.18913) | ETH | 同時估計相機內參的通用公制深度 | CVPR 2024 | 528 | [1,271](https://github.com/lpiccinelli-eth/UniDepth) |
| 主流 | 2023 | [Marigold](https://arxiv.org/abs/2312.02145) · [專案頁](https://marigoldmonodepth.github.io) | ETH | 把影像 diffusion 模型轉成深度估計器 | CVPR 2024 | 511 | [3,240](https://github.com/prs-eth/Marigold) |
| 主流 | 2025 | [MapAnything](https://arxiv.org/abs/2509.13414) · [專案頁](https://map-anything.github.io/) | Meta / CMU | 可接受多種輸入（內參、位姿、深度）的通用 feed-forward 重建 | arXiv | 377 | [3,817](https://github.com/facebookresearch/map-anything) |
| 主流 | 2024 | [MoGe](https://arxiv.org/abs/2410.19115) · [專案頁](https://wangrc.site/MoGePage/) | Microsoft | 單張影像估計仿射不變點雲 | CVPR 2025 | 369 | [3,049](https://github.com/microsoft/MoGe) |
| 主流 | 2025 | [π³](https://arxiv.org/abs/2507.13347) · [專案頁](https://yyfz.github.io/pi3/) | Shanghai AI Lab 等 | 無參考視角的置換等變 feed-forward 重建 | arXiv | 349 | [2,212](https://github.com/yyfz/Pi3) |
| 主流 | 2025 | [FoundationStereo](https://arxiv.org/abs/2501.09898) · [專案頁](https://nvlabs.github.io/FoundationStereo/) | NVIDIA | 零樣本雙目深度基礎模型 | CVPR 2025 | 315 | [2,949](https://github.com/NVlabs/FoundationStereo) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09 | [Scal3R](https://arxiv.org/abs/2609.04201) · [專案頁](https://linjohnss.github.io/scal3r/) | NYCU / NVIDIA | 多相對位姿 query 做可擴展的線上 3D 重建 |  | [GitHub](https://github.com/NVlabs/scal3r) | arXiv |
| 2026-09 | [Monocular Depth Estimation: Progress and Opportunities](https://arxiv.org/abs/2609.01172) | HKU | 單眼深度綜述 |  | [GitHub](https://github.com/CVMI-Lab/Depth_Survey) | arXiv |
| 2026-08 | [GeoFF3D](https://arxiv.org/abs/2608.28288) | Central South Univ. / NUDT | 座標錨定的 feed-forward 重建，用於大尺度 UAV 建圖 |  | [GitHub](https://github.com/yanxian-ll/GeoFF3D) | arXiv |
| 2026-07 | [The Multipath Blind Spot](https://arxiv.org/abs/2607.04101) | RKMVERI | 在凍結的深度基礎模型上，用稀疏錨點校正出公制深度 |  | 未公開 | arXiv |
| 2026-07 | [ARDepth](https://arxiv.org/abs/2607.12433) | SYSU / Baidu | 自回歸單眼深度估計 |  | 未公開 | arXiv |
| 2026-05 | [Focusable Monocular Depth Estimation](https://arxiv.org/abs/2605.11756) | SJTU / HKUST (GZ) | 區域導向深度：Depth Anything 2/3 負責幾何 + SAM3 選區域（相對深度） |  | 未公開 | arXiv |
| 2026-04 | [FreeOcc](https://arxiv.org/abs/2604.28115) · [專案頁](https://the-masses.github.io/freeocc-web/) | HKUST (GZ) / MBZUAI | 免訓練、具身、開放詞彙 occupancy 預測 |  | [GitHub](https://github.com/the-masses/FreeOcc) | arXiv |
| 2026-04 | [Feed-forward 3D scene modeling survey](https://arxiv.org/abs/2604.14025) · [專案頁](https://ff3d-survey.github.io) | Zhejiang / NTU / Monash / ETH / Tübingen | feed-forward 3D 重建綜述，涵蓋 Point3R、IncVGGT、ZipMap 等串流／增量版本 |  | [GitHub](https://github.com/ziplab/Awesome-Feed-Forward-3D) | arXiv |
| 2026-02 | [VGG-T³](https://arxiv.org/abs/2602.23361) · [專案頁](https://research.nvidia.com/labs/dvl/projects/vgg-ttt) | NVIDIA / Toronto | 大規模離線 feed-forward 重建 |  | [GitHub](https://github.com/nv-dvl/vgg-ttt) | CVPR 2026 |
| 2025-11 | [AMB3R](https://arxiv.org/abs/2511.20343) · [專案頁](https://hengyiwang.github.io/projects/amber) | UCL | feed-forward 公制尺度重建 + 稀疏體素後端，不微調即可延伸到 VO／SLAM |  | [GitHub](https://github.com/HengyiWang/amb3r) | CVPR 2026 |

## 電腦視覺（偵測、分割、視覺基礎模型）

### 在解決的問題

- 開放詞彙：偵測、分割不限類別（CLIP、Grounding DINO、SAM 3）。
- 通用視覺特徵：自監督預訓練（DINO）供深度、匹配、分割等下游任務。
- 即時性：能在機上跑（RT-DETR、YOLO-World）。
- 時序一致：點追蹤、影片分割（CoTracker、SAM 2）。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 奠基 | 2021 | [CLIP](https://arxiv.org/abs/2103.00020) | OpenAI | 影像-文字對比預訓練，開放詞彙感知的起點 | ICML 2021 | 57,726 | [34,471](https://github.com/openai/CLIP) |
| 奠基 | 2023 | [SAM](https://arxiv.org/abs/2304.02643) · [專案頁](https://segment-anything.com) | Meta | 可提示的通用分割基礎模型 | ICCV 2023 | 16,199 | [55,012](https://github.com/facebookresearch/segment-anything) |
| 奠基 | 2021 | [MAE](https://arxiv.org/abs/2111.06377) | Meta | 遮罩自編碼自監督預訓練 | CVPR 2022 | 13,184 | [8,361](https://github.com/facebookresearch/mae) |
| 奠基 | 2023 | [DINOv2](https://arxiv.org/abs/2304.07193) | Meta | 自監督視覺特徵，免微調可用於深度、分割、匹配 | TMLR 2024 | 11,297 | [13,430](https://github.com/facebookresearch/dinov2) |
| 奠基 | 2023 | [Grounding DINO](https://arxiv.org/abs/2303.05499) | IDEA | 語言引導的開放集合物件偵測 | ECCV 2024 | 5,263 | [10,676](https://github.com/IDEA-Research/GroundingDINO) |
| 奠基 | 2023 | [RT-DETR](https://arxiv.org/abs/2304.08069) · [專案頁](https://zhao-yian.github.io/RTDETR) | Baidu | 即時 DETR 偵測器 | CVPR 2024 | 4,683 | [5,598](https://github.com/lyuwenyu/RT-DETR) |
| 奠基 | 2024 | [SAM 2](https://arxiv.org/abs/2408.00714) · [專案頁](https://ai.meta.com/sam2) | Meta | 支援影片的可提示分割 | ICLR 2025 | 4,547 | [20,009](https://github.com/facebookresearch/sam2) |
| 奠基 | 2023 | [SigLIP](https://arxiv.org/abs/2303.15343) | Google | sigmoid 損失的影像-文字預訓練，多數 VLM 的視覺編碼器 | ICCV 2023 | 4,077 | [3,552](https://github.com/google-research/big_vision) |
| 奠基 | 2025 | [DINOv3](https://arxiv.org/abs/2508.10104) | Meta | 擴大規模並改善稠密特徵的自監督視覺模型 | arXiv | 1,742 | [11,550](https://github.com/facebookresearch/dinov3) |
| 奠基 | 2024 | [Grounded SAM](https://arxiv.org/abs/2401.14159) | IDEA | Grounding DINO + SAM 組合做開放詞彙分割 | arXiv | 1,365 | [17,758](https://github.com/IDEA-Research/Grounded-Segment-Anything) |
| 奠基 | 2023 | [LightGlue](https://arxiv.org/abs/2306.13643) | ETH | 快速自適應的特徵匹配，SLAM 前端常用 | ICCV 2023 | 1,272 | [4,829](https://github.com/cvg/LightGlue) |
| 奠基 | 2025 | [SAM 3](https://arxiv.org/abs/2511.16719) | Meta | 以概念（文字／範例）提示的分割與追蹤 | arXiv | 1,241 | [11,981](https://github.com/facebookresearch/sam3) |
| 奠基 | 2024 | [YOLO-World](https://arxiv.org/abs/2401.17270) | Tencent | 即時開放詞彙偵測 | CVPR 2024 | 1,136 | [6,585](https://github.com/AILab-CVC/YOLO-World) |
| 主流 | 2023 | [CoTracker](https://arxiv.org/abs/2307.07635) · [專案頁](https://co-tracker.github.io/) | Meta / Oxford | 聯合追蹤大量點的影片點追蹤 | ECCV 2024 | 688 | [5,153](https://github.com/facebookresearch/co-tracker) |
| 主流 | 2022 | [OWL-ViT](https://arxiv.org/abs/2205.06230) | Google | 用 CLIP 式骨幹做開放詞彙偵測 | ECCV 2022 | 455 | [3,842](https://github.com/google-research/scenic) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-04 | [OVS-DINO](https://arxiv.org/abs/2604.08461) | Tongji / PolyU 等 | 結構對齊 SAM 與 DINO 特徵，加語言引導做開放詞彙分割 |  | 未公開 | arXiv |
| 2026-03 | [dinov3.seg](https://arxiv.org/abs/2603.19531) | IIT Bombay / Monash | 凍結 DINOv3 + 訓練文字編碼器（dinov3.txt），加分割 adapter 做開放詞彙語意分割 |  | 未公開 | arXiv |
| 2026-02 | [Taming SAM3 in the Wild](https://arxiv.org/abs/2602.06333) | SKKU / SWJTU / NJUST 等 | 用 concept bank 校正 SAM3 的開放詞彙分割預測 |  | [GitHub](https://github.com/pgsmall/ConceptBank) | arXiv |

## Real2Sim 場景還原

### 在解決的問題

- 視覺擬真：模擬器畫面和真實影像有落差，改用 NeRF／3DGS 重建真實場景來渲染。
- 物理可用：重建的場景要有碰撞網格、關節、材質，才能互動與訓練。
- 低成本擷取：手機或手持相機掃描就能建。
- 在數位分身裡訓練或評估策略，再部署回實機（real-to-sim-to-real）。
- 另一路線是生成式 world model（如 Cosmos）直接產生訓練資料。

### 經典（近五年，資料日期 2026-10-15）

| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|
| 奠基 | 2022 | [Instant-NGP](https://arxiv.org/abs/2201.05989) · [專案頁](https://nvlabs.github.io/instant-ngp) | NVIDIA | 多解析度雜湊編碼，秒級訓練 NeRF | SIGGRAPH 2022 | 6,458 | [17,576](https://github.com/NVlabs/instant-ngp) |
| 奠基 | 2021 | [Isaac Gym](https://arxiv.org/abs/2108.10470) · [專案頁](https://sites.google.com/view/isaacgym-nvidia) | NVIDIA | GPU 端到端物理模擬，大規模平行 RL | NeurIPS 2021 | 2,035 | [2,952](https://github.com/isaac-sim/IsaacGymEnvs) |
| 奠基 | 2024 | [2D Gaussian Splatting](https://arxiv.org/abs/2403.17888) · [專案頁](https://surfsplatting.github.io) | ShanghaiTech / Tübingen | 幾何準確的表面重建，可輸出網格 | SIGGRAPH 2024 | 1,714 | [3,312](https://github.com/hbb1/2d-gaussian-splatting) |
| 奠基 | 2023 | [Nerfstudio](https://arxiv.org/abs/2302.04264) · [專案頁](https://nerf.studio) | UC Berkeley | 模組化 NeRF／3DGS 重建框架 | SIGGRAPH 2023 | 1,068 | [12,069](https://github.com/nerfstudio-project/nerfstudio) |
| 奠基 | 2025 | [Cosmos](https://arxiv.org/abs/2501.03575) · [專案頁](https://research.nvidia.com/labs/dir/cosmos1/) | NVIDIA | 物理 AI 的 world foundation model 平台 | arXiv | 953 | [12,042](https://github.com/NVIDIA/Cosmos) |
| 主流 | 2023 | [SuGaR](https://arxiv.org/abs/2311.12775) · [專案頁](https://anttwo.github.io/sugar/) | ENPC | 從 3DGS 抽出可編輯網格 | CVPR 2024 | 983 | [3,533](https://github.com/Anttwo/SuGaR) |
| 主流 | 2021 | [Habitat 2.0](https://arxiv.org/abs/2106.14405) | Meta | 可互動的室內重建場景模擬器，具身 AI 標準平台 | NeurIPS 2021 | 840 | [3,161](https://github.com/facebookresearch/habitat-lab) |
| 主流 | 2023 | [Orbit / Isaac Lab](https://arxiv.org/abs/2301.04195) · [專案頁](https://isaac-orbit.github.io/) | NVIDIA / ETH | 基於 Isaac Sim 的機器人學習框架 | RA-L 2023 | 622 | [8,351](https://github.com/isaac-sim/IsaacLab) |
| 主流 | 2024 | [gsplat](https://arxiv.org/abs/2409.06765) · [專案頁](https://docs.gsplat.studio/) | UC Berkeley | 開源 CUDA 高斯潑濺函式庫 | JMLR 2025 | 406 | [5,794](https://github.com/nerfstudio-project/gsplat) |
| 新興 | 2024 | [RialTo](https://arxiv.org/abs/2403.03949) · [專案頁](https://real-to-sim-to-real.github.io/RialTo/) | MIT | 真實場景重建成模擬環境，在模擬中強化學習修正策略 | RSS 2024 | 236 | [0](https://github.com/real-to-sim-to-real/RialToPolicyLearning) |
| 新興 | 2024 | [SplatSim](https://arxiv.org/abs/2409.10161) · [專案頁](https://splatsim.github.io) | CMU | 用 3DGS 取代模擬器渲染，縮小視覺 sim-to-real 差距 | ICRA 2025 | 103 | [0](https://github.com/qureshinomaan/SplatSim) |
| 新興 | 2025 | [VR-Robo](https://arxiv.org/abs/2502.01536) · [專案頁](https://vr-robo.github.io/) | Tsinghua | 3DGS 重建場景做視覺導航與運動控制的 real-to-sim-to-real | RA-L 2025 | 36 | [0](https://github.com/zst1406217/VR-Robo) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [Digital Twin-Driven Real2Sim2Real](https://arxiv.org/abs/2610.08339) | TUM / Hyundai / MORAI | 自駕場景成對重建，以模擬器條件生成訓練影像（非物理互動場景） |  | 未公開 | arXiv |
| 2026-09 | [ReVeal](https://arxiv.org/abs/2609.23910) | Purdue / Samsung SDS | 考慮重建品質的 real-to-sim VLA 策略評估 |  | 未公開 | arXiv |
| 2026-06 | [ArtiTwinSplat](https://arxiv.org/abs/2606.24628) | ETH / Microsoft / Bonn | 手持 RGB-D 影片重建可互動數位分身（3DGS），輸出碰撞網格、門／抽屜關節、URDF，可直接匯入 Isaac Sim |  | 未公開 | arXiv |
| 2026-06 | [Robots Need More than VLA and World Models](https://arxiv.org/abs/2606.06556) | Motoniq.ai / Stanford / ETH 等 | 立場論文；整理 3DGS 模擬器訓練的導航策略可 zero-shot 轉移到實機（SOUS VIDE、SINGER、GRaD-Nav） |  | 未公開 | arXiv |
| 2026-03 | [SimRecon](https://arxiv.org/abs/2603.02133) · [專案頁](https://xiac20.github.io/SimRecon/) | Tsinghua / Galbot | 從真實影片做 SimReady 的組合式場景重建 |  | [GitHub](https://github.com/xiac20/SimRecon) | arXiv |
| 2025-12 | [PolaRiS](https://arxiv.org/abs/2512.16881) · [專案頁](https://polaris-evals.github.io/) | UW / UC Berkeley / Stanford / TRI / Physical Intelligence 等 | 可擴展的 real-to-sim 通用策略評估 |  | [GitHub](https://github.com/arhanjain/polaris) | arXiv |
| 2025-09 | [EmbodiedSplat](https://arxiv.org/abs/2509.17430) · [專案頁](https://gchhablani.github.io/embodied-splat) | Georgia Tech / TRI | 手機掃描建 3DGS 場景，在 Habitat-Sim 裡微調導航策略後部署回實機 |  | [GitHub](https://github.com/gchhablani/embodied-splat-v1) | arXiv |

## 月報

- [2026-10](digests/2026-10.md)

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 後重跑 -->

# 四足

## 在解決的問題

- 感知不可靠時仍要穩（反光、草叢、高度圖雜訊）：融合外部感知與本體感知。
- sim-to-real：大規模平行模擬 + domain randomization + 特權教師蒸餾。
- 敏捷技能（跑酷、跳躍、越溝）與技能切換。
- 從「跟隨速度指令」走向「運動與導航一體」，直接走到目標。

## 重要論文（資料日期 2026-11-01）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、獲獎 | 2022 | [Perceptive Locomotion in the Wild](https://arxiv.org/abs/2201.08117) | ETH | 高度圖感知 + 本體感知的注意力融合，ANYmal 野外實機 | Science Robotics 2022 | 1,290 | 未公開 |
| 奠基 | 引用、Star | 2021 | [Learning to Walk in Minutes](https://arxiv.org/abs/2109.11978) · [專案頁](https://leggedrobotics.github.io/legged_gym/) | ETH | GPU 大規模平行 RL，幾分鐘訓練出運動策略（legged_gym） | CoRL 2021 | 1,211 | [3,169](https://github.com/leggedrobotics/legged_gym) |
| 主流 | 引用 | 2021 | [RMA](https://arxiv.org/abs/2107.04034) · [專案頁](https://ashish-kmr.github.io/rma-legged-robots/) | UC Berkeley / CMU | 快速自適應模組：以本體感知線上估計環境參數 | RSS 2021 | 1,161 | 未公開 |
| 主流 | 引用、機構 | 2022 | [DayDreamer](https://arxiv.org/abs/2206.14176) · [專案頁](https://danijar.com/daydreamer) | UC Berkeley | 世界模型讓實體機器人免模擬器直接在線學習 | CoRL 2022 | 646 | [469](https://github.com/danijar/daydreamer) |
| 主流 | 引用、獲獎 | 2023 | [ANYmal Parkour](https://arxiv.org/abs/2306.14874) · [專案頁](https://sites.google.com/leggedrobotics.com/agile-navigation) | ETH | 感知、移動、技能選擇分模組的跑酷導航 | Science Robotics 2024 | 498 | 未公開 |
| 主流 | 引用、Star | 2023 | [Extreme Parkour](https://arxiv.org/abs/2309.14341) · [專案頁](https://extreme-parkour.github.io/) | CMU | 單一神經網路以深度相機做極限跑酷 | ICRA 2024 | 432 | [1,188](https://github.com/chengxuxin/extreme-parkour) |
| 主流 | 引用、機構 | 2022 | [Rapid Locomotion](https://arxiv.org/abs/2205.02824) · [專案頁](https://agility.csail.mit.edu/) | MIT | 自適應課程 RL 讓 Mini Cheetah 跑出紀錄速度 | RSS 2022 | 428 | [302](https://github.com/Improbable-AI/rapid-locomotion-rl) |
| 主流 | 引用、獲獎 | 2022 | [Legged Locomotion with Egocentric Vision](https://arxiv.org/abs/2211.07638) · [專案頁](https://vision-locomotion.github.io) | CMU / Berkeley | 直接用深度影像端到端學運動，不建高度圖 | CoRL 2022 | 371 | 未公開 |
| 主流 | 引用、Star、獲獎 | 2023 | [Robot Parkour Learning](https://arxiv.org/abs/2309.05665) · [專案頁](https://robot-parkour.github.io) | Stanford / Shanghai Qi Zhi | 低成本四足以深度相機學跑酷技能 | CoRL 2023 | 352 | [1,142](https://github.com/ZiwenZhuang/parkour) |
| 主流 | 引用、Star | 2022 | [Walk These Ways](https://arxiv.org/abs/2212.03238) · [專案頁](https://gmargo11.github.io/walk-these-ways/) | MIT | 多樣行為參數化的單一策略，可調步態 | CoRL 2022 | 349 | [1,470](https://github.com/Improbable-AI/walk-these-ways) |
| 主流 | 引用、獲獎 | 2022 | [Legged Optimization Control Survey](https://arxiv.org/abs/2211.11644) | Notre Dame / UPenn / LAAS-CNRS 等 | 回顧足式機器人模型式最佳化控制的綜述 | T-RO 2024 | 322 | 未公開 |
| 主流 | 引用、獲獎、知名 | 2022 | [Perceptive NMPC](https://arxiv.org/abs/2208.08373) | ETH | 以凸落腳區約束嵌入全身 NMPC 的感知式運動 | T-RO 2023 | 320 | 未公開 |
| 主流 | 引用 | 2023 | [DreamWaQ](https://arxiv.org/abs/2301.10602) · [專案頁](https://sites.google.com/view/dreamwaq) | KAIST | 無外部感知的盲走策略，用隱式地形想像過複雜地形 | ICRA 2023 | 266 | 未公開 |
| 主流 | 引用、獲獎 | 2023 | [Locomotion on Deformable Terrain](https://doi.org/10.1126/scirobotics.ade2256) | KAIST | 在沙地等可變形地形上的四足 RL 運動，模擬可變形接觸 | Science Robotics 2023 | 262 | 未公開 |
| 主流 | Star | 2022 | [Elevation Mapping CuPy](https://arxiv.org/abs/2204.12876) · [專案頁](https://leggedrobotics.github.io/elevation_mapping_cupy/) | ETH | GPU 加速的機器人中心高度圖，多數感知式運動策略的輸入 | IROS 2022 | 212 | [1,154](https://github.com/leggedrobotics/elevation_mapping_cupy) |
| 主流 | 引用、獲獎 | 2023 | [DTC](https://arxiv.org/abs/2309.15462) | ETH | RL 策略追蹤軌跡最佳化參考，兼顧精準與強健 | Science Robotics 2024 | 205 | 未公開 |
| 主流 | 引用、Star、HF、獲獎 | 2024 | [ABS](https://arxiv.org/abs/2401.17583) · [專案頁](https://agile-but-safe.github.io/) | CMU | 敏捷策略 + 學到的可達避碰價值函數，高速且安全 | RSS 2024 | 187 | [630](https://github.com/LeCAR-Lab/ABS) |
| 主流 | 引用、獲獎 | 2023 | [Legged Planetary Exploration Team](https://arxiv.org/abs/2307.10079) | ETH | 多隻技能互補的四足機器人團隊探勘行星類比地形 | Science Robotics 2023 | 168 | 未公開 |
| 主流 | 引用、Star、機構 | 2024 | [DrEureka](https://arxiv.org/abs/2406.01967) · [專案頁](https://eureka-research.github.io/dr-eureka/) | UPenn / NVIDIA / UT Austin | LLM 自動設計獎勵與域隨機化參數做 sim-to-real | RSS 2024 | 147 | [947](https://github.com/eureka-research/DrEureka) |
| 主流 | 引用、Star、獲獎、機構 | 2024 | [DIAL-MPC](https://arxiv.org/abs/2409.15610) · [專案頁](https://lecar-lab.github.io/dial-mpc/) | CMU | 擴散式退火取樣 MPC，免訓練做全階力矩控制 | ICRA 2025 | 121 | [1,012](https://github.com/LeCAR-Lab/dial-mpc) |
| 主流 | 引用、獲獎 | 2025 | [Attention Map Encoding](https://arxiv.org/abs/2506.09588) | ETH / Disney Research | 以本體感知為條件的注意力地圖編碼，泛化稀疏落腳地形 | Science Robotics 2025 | 108 | 未公開 |
| 主流 | 引用 | 2024 | [PIE](https://arxiv.org/abs/2408.13740) | Zhejiang | 單階段隱式＋顯式雙層估計的端到端跑酷策略 | RA-L 2024 | 93 | 未公開 |
| 主流 | 引用、機構 | 2024 | [DiffuseLoco](https://arxiv.org/abs/2404.19264) · [專案頁](https://diffuselo.co/) | UC Berkeley / Simon Fraser | 從離線資料訓練擴散策略並即時跑在實機 | CoRL 2024 | 84 | [200](https://github.com/HybridRobotics/DiffuseLoco) |
| 主流 | 引用 | 2025 | [Parkour in the Wild](https://arxiv.org/abs/2505.11164) | ETH RSL | 多專家策略蒸餾後再 RL 微調的通用敏捷運動 | IJRR 2026 | 70 | 未公開 |
| 主流 | 引用、獲獎 | 2025 | [High-Speed Legged Navigation](https://arxiv.org/abs/2506.02835) | KAIST | 取樣式落腳規劃加物理模擬篩選的高速離散地形導航 | Science Robotics 2025 | 66 | 未公開 |
| 主流 | 引用、機構 | 2025 | [MoE-Loco](https://arxiv.org/abs/2503.08564) · [專案頁](https://moe-loco.github.io/) | Tsinghua / Shanghai Qi Zhi / MIT | 混合專家緩解多任務 RL 梯度衝突，單策略跨地形 | IROS 2025 | 54 | [62](https://github.com/hrh6666/MoE-Loco) |
| 主流 | 引用、獲獎 | 2025 | [LocoFormer](https://arxiv.org/abs/2509.23745) | Skild AI | 在程序生成的大量機體上做長上下文 RL，測試時靠歷史自行適應未見過的腿式與輪式機體 | CoRL 2025 | 38 | 未公開 |
| 主流 | 引用 | 2025 | [TRG-planner](https://arxiv.org/abs/2501.01806) · [專案頁](https://trg-planner.github.io/) | KAIST | 以穿越風險圖兼顧地形安全與距離的路徑規劃 | RA-L 2025 | 37 | [31](https://github.com/wasahaiah/TRG-planner) |
| 主流 | 引用、機構 | 2025 | [SPI-Active](https://arxiv.org/abs/2505.14266) · [專案頁](https://lecar-lab.github.io/spi-active_/) | CMU / Google DeepMind | 取樣式系統辨識加主動探索縮小 sim-to-real 差距 | CoRL 2025 | 34 | [231](https://github.com/LeCAR-Lab/SPI-Active) |
| 主流 | 引用、獲獎 | 2025 | [Unified Force-Position Policy](https://arxiv.org/abs/2505.20829) · [專案頁](https://unified-force.github.io/) | BUPT / BIGAI | 不靠力感測器，單一策略同時建模接觸力與位置控制，用於四足帶手臂的接觸型移動操作 | CoRL 2025 | 32 | 未公開 |
| 新興 | 獲獎、知名 | 2022 | [AMP for Locomotion](https://arxiv.org/abs/2203.15103) | UC Berkeley / Google | 用對抗式動作先驗取代繁瑣的手調獎勵，四足實機學出自然且節能的步態 | IROS 2022 | 206 | 未公開 |
| 新興 | 獲獎 | 2026 | [DAWN](https://arxiv.org/abs/2609.29092) · [專案頁](https://dawn-parkour.github.io/) | KOREATECH | 在 world model 裡學習去除深度雜訊，跑酷策略不需手調深度濾波器 | IROS 2026 | 1 | 未公開 |

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [End-to-End RL for Quadrupedal Jumping in Lunar Gravity](https://arxiv.org/abs/2610.29586) | ETH RSL | 多階段 RL 訓練單一端到端策略，只用任務可用的機載感測做指定點跳躍 | 模擬落點誤差小於機身尺寸；月球重力卸載下實機垂直跳 | 未公開 | arXiv |

更早的 4 篇見 [topics/quadruped.md](../topics/quadruped.md)。

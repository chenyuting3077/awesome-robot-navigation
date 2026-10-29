<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 後重跑 -->

# 輪足（雙足輪、四足輪）

## 在解決的問題

- 混合運動：何時滾、何時走、何時跨越，以及模式切換。
- 高速下的感知延遲：建圖更新跟不上速度（Lee et al. 2024 指出這限制了自主時的速度）。
- 硬體負載：輪驅動改變關節受力（Go2-W 髖關節過熱）。
- 雙足輪的平衡與越障；研究多停在運動控制，經典論文少。

## 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、獲獎 | 2024 | [Wheeled-Legged Urban Navigation](https://arxiv.org/abs/2405.01792) | ETH | 階層式 RL 導航 + 運動，都市公里級自主任務 | Science Robotics 2024 | 217 | 未公開 |
| 新興 | 獲獎 | 2022 | [Track-leg / Wheel-leg TrajOpt](https://doi.org/10.1109/ICRA46639.2022.9812199) | Florida State | 具平滑解析導數的軌跡最佳化，讓履帶腿、輪腿機器人規劃翻越大型障礙 | ICRA 2022 | 4 | 未公開 |

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [RAIWAY](https://arxiv.org/abs/2610.33172) | KAIST | 20 吋大輪雙足輪機器人；在模擬中把多接觸事件蒸餾成潛變量，部署時只用本體感測推估，不需接觸感測 | 實機通過陡坡、碎石、釘面、岩地，與最高 15 cm 階高的戶外階梯 | 未公開 | RA-L 2026 |
| 2026-02 | [Sparse MoE multi-mode locomotion](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1788395/full) | Beijing Institute of Technology | 雙足輪；稀疏 MoE RL，在滾動與越障間自動切換 |  | 未公開 | Frontiers in Robotics and AI 2026 |

# 輪足（雙足輪、四足輪）

## 在解決的問題

- 混合運動：何時滾、何時走、何時跨越，以及模式切換。
- 高速下的感知延遲：建圖更新跟不上速度（Lee et al. 2024 指出這限制了自主時的速度）。
- 硬體負載：輪驅動改變關節受力（Go2-W 髖關節過熱）。
- 雙足輪的平衡與越障；研究多停在運動控制，經典論文少。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | [Traversal Risk Graph Planning](https://arxiv.org/abs/2608.16433) | ShanghaiTech | 考慮機身的穿越風險圖規劃 |  | [GitHub](https://github.com/ZhiqiaoGuo/RB-TRG) | arXiv |
| 2026-06 | [Go2-W Long-Distance Navigation](https://arxiv.org/abs/2606.21387) | Chiba Tech fuRo | 輪子驅動會讓髖關節過熱，訓練能分散負載的策略 | Tsukuba Challenge 2025 自主約 2.8 km（人行道、公園、樓梯） | 未公開 | arXiv |
| 2026-04 | [Reflexive Obstacle Evasion](https://arxiv.org/abs/2604.23761) · [專案頁](https://aware-ral-2026.github.io/) | Tianjin Univ. / Zhongguancun Academy / NUS | 輪足高動態反射式閃避 |  | 未公開 | arXiv |
| 2026-02 | [Sparse MoE multi-mode locomotion](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1788395/full) | Beijing Institute of Technology | 雙足輪；稀疏 MoE RL，在滾動與越障間自動切換 |  | 未公開 | Frontiers in Robotics and AI 2026 |

# 局部導航策略（diffusion / world model）

## 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 來源 |
|---|---|---|---|---|---|
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | arXiv |
| 2026-08 | [UniNav](https://arxiv.org/abs/2608.03244) | HKUST (GZ) / CUHK-SZ | 統一 world-action diffusion | arXiv |
| 2026-08 | [ODG-NoMaD](https://arxiv.org/abs/2608.21395) | 論文未標示 | NoMaD 加俯視相機方向引導 | arXiv |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) | Shanghai AI Lab / Fudan / SYSU | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） | arXiv |
| 2026-06 | [NavWM](https://arxiv.org/abs/2606.24101) | CASIA / Beihang | 導航 world model 做前瞻規劃 | arXiv |
| 2026-06 | [NavWAM](https://arxiv.org/abs/2606.13494) | Univ. of Tokyo | goal-conditioned world action model | arXiv |
| 2026-05 | [NavOL](https://arxiv.org/abs/2605.11762) | Fudan / Shanghai Innovation Institute | diffusion 導航策略在 IsaacLab 線上模仿學習，解 NavDP 離線資料限制 | arXiv |
| 2026-03 | [Beyond Imitation](https://arxiv.org/abs/2603.12868) | NTU / A*STAR / NUS | RL 微調 diffusion 導航策略 | arXiv |

# 局部導航與規劃（diffusion / world model / 探索）

## 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

## 最新論文

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

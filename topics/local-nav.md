# 局部導航與規劃（diffusion / world model / 探索）

## 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [RangeNav](https://arxiv.org/abs/2610.29845) · [專案頁](https://rangenav.github.io/) | ETH Zurich RSL / NVIDIA | 用導航對齊目標（距離圖重建 + 語意分割 + BEV 預測）預訓練 183k 參數 LiDAR range-image 編碼器，凍結後給 RL 策略用 | 模擬中加入語意與 BEV 監督，成功率平均比只做重建高 32.03 / 23.73 pp（訓練環境 / OOD 環境）；Unitree B2-W 零樣本實機通過人群、低光與工地 | 未公開 | arXiv |
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 未公開 | arXiv |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) · [專案頁](https://yty-sky.github.io/x-navdp-project-page) | Shanghai AI Lab / Fudan / SYSU | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） |  | 未公開 | arXiv |

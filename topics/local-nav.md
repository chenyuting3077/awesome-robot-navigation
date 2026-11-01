# 局部導航與規劃（diffusion / world model / 探索）

## 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [TravSUITE](https://arxiv.org/abs/2610.32130) | CMU / Field AI | 越野高速導航的可通行性系統：高效 voxel mapper 加自監督、含不確定性的 IRL，部署時依風險調整 | 實機導航錯誤減少 80%、穿越速度快 5% | 未公開 | RSS 2026 |
| 2026-08 | [ULVN](https://arxiv.org/abs/2608.06833) · [專案頁](https://hren20.github.io/ulvn-website) | Sun Yat-sen / Insta360 Research | 影像目標導航不需時序影片或深度：從無序影像建圖，用圖上信念傳播定位與規劃子目標；有實機部署 |  | [GitHub](https://github.com/hren20/ulvn) | ECCV 2026 |
| 2026-06 | [A scalar per patch](https://arxiv.org/abs/2606.21216) | NAVER LABS Europe | 大規模實機比較視覺編碼器，發現每個 patch 壓到單一純量仍足以支撐導航，且特徵可對應 affordance | 實體建築 966 個 episode、24 km | 未公開 | ECCV 2026 |
| 2026-03 | [RAE-NWM](https://arxiv.org/abs/2603.09241) | Tsinghua | 導航 world model 改在稠密 DINOv2 特徵空間做時序預測，不用壓縮後的 VAE latent，保留細部結構 |  | [GitHub](https://github.com/20robo/raenwm) | ECCV 2026 |
| 2025-10 | [UniWM](https://arxiv.org/abs/2510.08713) | University of Washington | 單一自迴歸骨幹同時做視覺預想與規劃，讓動作選擇直接依據想像結果，並加入記憶 | 導航成功率最高提升 30% | [GitHub](https://github.com/UWMILab/UniWM) | ECCV 2026 |
| 2026-10 | [RangeNav](https://arxiv.org/abs/2610.29845) · [專案頁](https://rangenav.github.io/) | ETH RSL / NVIDIA | 只用合成資料預訓練 183k 參數的 LiDAR range-image encoder（重建 + 語意分割 + BEV 預測），凍結後給 RL 導航策略 | 模擬 SR 比僅重建基線平均高 32.03 / 23.73 pp（訓練／OOD 環境）；Unitree B2-W 零樣本實機過人群與工地 | 未公開 | arXiv |
| 2026-10 | [Physical AI for Intralogistics](https://arxiv.org/abs/2610.28432) | Idealworks / NVIDIA | 把 NVIDIA X-Mobility 與 COMPASS 導航策略放進倉儲數位孿生訓練，再用 Cosmos 生成 sim-to-real 變體資料微調，部署在 Jetson AGX Xavier 差速底盤 | 實機四個場景成功率 65.3%（純模擬訓練）→ 91.7%（加 Cosmos 資料），與量產導航堆疊差 8.3 點 | 未公開 | arXiv |
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 未公開 | arXiv |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) · [專案頁](https://yty-sky.github.io/x-navdp-project-page) | Shanghai AI Lab / Fudan / SYSU | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） |  | 未公開 | arXiv |

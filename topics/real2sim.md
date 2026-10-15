# Real2Sim 場景還原

## 在解決的問題

- 視覺擬真：模擬器畫面和真實影像有落差，改用 NeRF／3DGS 重建真實場景來渲染。
- 物理可用：重建的場景要有碰撞網格、關節、材質，才能互動與訓練。
- 低成本擷取：手機或手持相機掃描就能建。
- 在數位分身裡訓練或評估策略，再部署回實機（real-to-sim-to-real）。
- 另一路線是生成式 world model（如 Cosmos）直接產生訓練資料。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 來源 |
|---|---|---|---|---|---|
| 2026-10 | [Digital Twin-Driven Real2Sim2Real](https://arxiv.org/abs/2610.08339) | TUM / Hyundai / MORAI | 自駕場景成對重建，以模擬器條件生成訓練影像（非物理互動場景） | arXiv |
| 2026-09 | [ReVeal](https://arxiv.org/abs/2609.23910) | Purdue / Samsung SDS | 考慮重建品質的 real-to-sim VLA 策略評估 | arXiv |
| 2026-06 | [ArtiTwinSplat](https://arxiv.org/abs/2606.24628) | ETH / Microsoft / Bonn | 手持 RGB-D 影片重建可互動數位分身（3DGS），輸出碰撞網格、門／抽屜關節、URDF，可直接匯入 Isaac Sim | arXiv |
| 2026-06 | [Robots Need More than VLA and World Models](https://arxiv.org/abs/2606.06556) | Motoniq.ai / Stanford / ETH 等 | 立場論文；整理 3DGS 模擬器訓練的導航策略可 zero-shot 轉移到實機（SOUS VIDE、SINGER、GRaD-Nav） | arXiv |
| 2026-03 | [SimRecon](https://arxiv.org/abs/2603.02133) | Tsinghua / Galbot | 從真實影片做 SimReady 的組合式場景重建 | arXiv |
| 2025-12 | [PolaRiS](https://arxiv.org/abs/2512.16881) | UW / UC Berkeley / Stanford / TRI / Physical Intelligence 等 | 可擴展的 real-to-sim 通用策略評估 | arXiv |
| 2025-09 | [EmbodiedSplat](https://arxiv.org/abs/2509.17430) | Georgia Tech / TRI | 手機掃描建 3DGS 場景，在 Habitat-Sim 裡微調導航策略後部署回實機 | arXiv |

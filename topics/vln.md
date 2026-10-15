# VLN 與導航基礎模型

## 在解決的問題

- 語言對應到空間：把「走到廚房冰箱旁」對到畫面與地圖上的位置。
- 長程、部分可觀測：指令長、環境沒看過，需要記憶與探索。
- sim-to-real：benchmark 多在 Habitat 模擬，實機成功率落差大。
- 推論延遲：數 B 參數的 VLM 難以機上即時跑，近期多改成「慢 VLM 推理 + 快控制層」。
- 跨機體：同一模型用在輪式、四足、人形。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 來源 |
|---|---|---|---|---|---|
| 2026-07 | [Robostral Navigate](https://arxiv.org/abs/2607.20785) | Mistral AI | 8B VLM 只用單眼 RGB，在畫面上指出下一個目標點；目標不在視野時輸出局部座標位移 | R2R-CE val-unseen SR 76.6%；online RL +3.2% | arXiv、Mistral 官網 |
| 2026-07 | [ABot-N1](https://arxiv.org/abs/2607.10383) | Alibaba AMAP | 慢 VLM 推理出影像錨點，快模組轉成連續 waypoint；同一架構做 point/object/POI/指令/跟人五種任務 | 室內 95.4%、室外 92.9% SR；POI 抵達 77.3% | arXiv |
| 2026-07 | [GemNav](https://arxiv.org/abs/2607.06882) | CSIRO | MLLM 輸出離散 token 當導航動作 | arXiv |
| 2026-04 | [Robot Navigation via Foundation Language Models: A Review](https://dl.acm.org/doi/10.1145/3802539) | ECNU / HIT 等 | ACM CSUR 綜述 | ACM Computing Surveys 2026 |

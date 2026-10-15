# VLN 與導航基礎模型

| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |
|---|---|---|---|---|---|
| 2026-07 | [Robostral Navigate](https://arxiv.org/abs/2607.20785) | Mistral AI | 8B VLM 只用單眼 RGB，在畫面上指出下一個目標點；目標不在視野時輸出局部座標位移 | R2R-CE val-unseen SR 76.6%；online RL +3.2% | 摘要 |
| 2026-07 | [ABot-N1](https://arxiv.org/abs/2607.10383) | Alibaba AMAP | 慢 VLM 推理出影像錨點，快模組轉成連續 waypoint；同一架構做 point/object/POI/指令/跟人五種任務 | 室內 95.4%、室外 92.9% SR；POI 抵達 77.3% | 摘要 |
| 2026-07 | [GemNav](https://arxiv.org/abs/2607.06882) | | MLLM 輸出離散 token 當導航動作 | | 標題 |
| 2026-04 | [Robot Navigation via Foundation Language Models: A Review](https://dl.acm.org/doi/10.1145/3802539) | | ACM CSUR 綜述 | | 標題 |
| 2024-12 | [NaVILA](https://arxiv.org/abs/2412.04453) | UCSD / NVIDIA / USC | VLM 輸出中層語言動作，低層運動策略執行；換低層策略即可換機體 | 實機 25 指令 88% SR | 摘要 |

# VLN 與導航基礎模型

## 在解決的問題

- 語言對應到空間：把「走到廚房冰箱旁」對到畫面與地圖上的位置。
- 長程、部分可觀測：指令長、環境沒看過，需要記憶與探索。
- sim-to-real：benchmark 多在 Habitat 模擬，實機成功率落差大。
- 推論延遲：數 B 參數的 VLM 難以機上即時跑，近期多改成「慢 VLM 推理 + 快控制層」。
- 跨機體：同一模型用在輪式、四足、人形。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [SimpleVLN](https://arxiv.org/abs/2610.23203) · [專案頁](https://simplevln.github.io/) | 復旦大學、南洋理工大學、Lenovo Research | 不改 MLLM 架構，用單輪決策輸入加固定長度全域＋局部記憶與 action chunk，訓練走 IL、DAgger、RL 三段 | R2R-CE SR 76.7%、RxR-CE SR 80.1% | 未公開 | arXiv |
| 2026-10 | [PASS-VLN](https://arxiv.org/abs/2610.22812) | Qiyuan Lab、清華大學 | 固定場景與路線、只改變機器人車寬的局部指令 VLN 基準；以障礙物膨脹把車寬編進深度導出的局部鳥瞰圖，預測離散潛在動作碼 | 無障礙成功率比微調後的強 VLN 基線高約 12 個百分點；有真機部署 | 未公開 | arXiv |
| 2026-10 | [AVALON](https://arxiv.org/abs/2610.21586) | HKU | 只需平面圖與地點線索，以人給的分層拓撲記憶做節點驗證式導航，不建全域 SLAM 圖；人與機器人共同更新記憶 | Unitree Go2 實機 12.81 m 任務 46.4 s（5/5），比 DimOS-Go2 少 40.9% 時間 | 未公開 | arXiv |
| 2026-07 | [Robostral Navigate](https://arxiv.org/abs/2607.20785) · [專案頁](https://mistral.ai/news/robostral-navigate) | Mistral AI | 8B VLM 只用單眼 RGB，在畫面上指出下一個目標點；目標不在視野時輸出局部座標位移 | R2R-CE val-unseen SR 76.6%；online RL +3.2% | 未公開 | arXiv、Mistral 官網 |
| 2026-07 | [ABot-N1](https://arxiv.org/abs/2607.10383) · [專案頁](https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/) | Alibaba AMAP | 慢 VLM 推理出影像錨點，快模組轉成連續 waypoint；同一架構做 point/object/POI/指令/跟人五種任務 | 室內 95.4%、室外 92.9% SR；POI 抵達 77.3% | [GitHub](https://github.com/amap-cvlab/ABot-Navigation) | arXiv |
| 2026-07 | [GemNav](https://arxiv.org/abs/2607.06882) | CSIRO | MLLM 輸出離散 token 當導航動作 |  | 未公開 | arXiv |
| 2026-04 | [Robot Navigation via Foundation Language Models: A Review](https://dl.acm.org/doi/10.1145/3802539) | ECNU / HIT 等 | ACM CSUR 綜述 |  | 未公開 | ACM Computing Surveys 2026 |

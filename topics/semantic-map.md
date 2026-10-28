# 語意地圖與場景圖

## 在解決的問題

- 開放詞彙：不限定類別，能用任意語言查物件與區域。
- 可擴展：稠密特徵地圖太大，改用物件／房間／樓層的階層場景圖壓縮。
- 即時、增量：邊走邊建，並處理場景變動。
- 當成 LLM／VLM 規劃的介面。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [OASIS](https://arxiv.org/abs/2610.30589) · [專案頁](https://starry-curry-30.github.io/oasis-project) | Beihang Univ. | 以少量穩定語意錨點節點建立線上地圖，每個節點整合語意描述、視覺特徵與幾何，支援開放詞彙檢索並在場景變動後重新定位被移動的物件 |  | [GitHub](https://github.com/starry-curry-30/OASIS) | ACM MM 2026 |
| 2026-10 | [AOV-GS](https://arxiv.org/abs/2610.29374) | MIPT / AIRI | 主動 3D Gaussian 建圖：以 SAM 實例的 CLIP 嵌入新穎度重排候選視角，不需人工標註遮罩 | 同樣 SAM-CLIP 下語言場 mIoU 比純幾何探索高 1.3 pp（Replica 34.6%）、1.8 pp（Matterport3D 23.1%） | [GitHub](https://github.com/OptimusFaber/AOV-GS) | AIST 2026 |
| 2026-05 | [LEXI-SG](https://arxiv.org/abs/2605.13741) · [專案頁](https://ori-drs.github.io/lexisg-web/) | Oxford | 只用單眼 RGB 建開放詞彙 3D 場景圖，以房間為單位 feed-forward 重建 | 評估在 HM3D 與自錄辦公室序列，未做實機導航 | 未公開 | RA-L 2026 |

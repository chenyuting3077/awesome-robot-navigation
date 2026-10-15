# 更新規則

- 一律用繁體中文（台灣用語）；commit message 用英文、conventional 前綴（`docs: ...`）。
- 範圍：AMR（輪式）、四足、輪足的導航，以及機器人用得到的視覺、3D 感知、SLAM、Real2Sim。純操作（manipulation）、純人形全身控制、純自駕不收，除非方法可直接用在上述機體。

## 主題邊界

一篇只放一個主題，以主要貢獻判斷：

- `vln.md`：用語言或高階目標下指令的導航，含導航基礎模型、VLA。
- `local-nav.md`：從感測器到軌跡或速度的局部導航策略（diffusion、world model、RL）。
- `semantic-map.md`：給導航查詢用的語意地圖、場景圖。
- `quadruped.md` / `wheel-legged.md`：該機體特有的運動控制與導航。
- `slam.md`：SLAM、VO、LIO、重定位、回環。
- `perception-3d.md`：深度估計、feed-forward 3D 重建、occupancy；沒有做定位的才放這裡，有做的放 slam。
- `vision.md`：2D 偵測、分割、追蹤、視覺基礎模型。
- `real2sim.md`：把真實場景重建成可模擬、可訓練或可評估策略的環境。

## 搜尋方式

0. **先查重點來源**（最優先）：arXiv API 無法依機構篩選，所以先逐一查下列來源的近期發表，再做第 1 步。
   - **NVIDIA**（每次都要查）：
     - https://research.nvidia.com/research-area/robotics 、 https://research.nvidia.com/research-area/computer-vision ：依年份列出論文，只顯示年份，月份看論文網址 slug。網站常比 arXiv 晚上架，所以兩邊都要查。
     - https://research.nvidia.com/publications ：全部論文，`?page=N` 翻頁，只能依會議篩選（例如 CoRL `?f%5B0%5D=publication_events%3A35`），不能依領域篩選。
     - 實驗室：Seattle Robotics Lab https://research.nvidia.com/labs/srl 、GEAR https://research.nvidia.com/labs/gear/ 。
     - 程式碼：https://github.com/NVlabs 。
     - 再用 WebSearch `NVIDIA <主題關鍵字> <年月>` 補查 Isaac、Cosmos、GR00T 等產品線的技術報告。
     - research.nvidia.com/labs/ 首頁會擋爬蟲（403），直接用上面的子頁。
   - **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba（AMAP、DAMO）、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics。
   - **實驗室**（括號內為主要相關主題）：
     - ETH RSL https://rsl.ethz.ch （四足、輪足）、ETH ASL https://asl.ethz.ch （SLAM、導航）
     - MIT SPARK https://web.mit.edu/sparklab/ （SLAM、場景圖）
     - CMU AirLab https://theairlab.org （SLAM、導航）
     - Berkeley RAIL https://rail.eecs.berkeley.edu （導航基礎模型）
     - UCSD Xiaolong Wang https://xiaolonw.github.io （腿式 VLA）
     - PKU EPIC https://pku-epic.github.io （VLN）
     - 上海 AI Lab InternRobotics https://github.com/InternRobotics （局部導航）
     - Oxford VGG https://www.robots.ox.ac.uk/~vgg/ （3D 重建）、Oxford DRS https://dynamic.robots.ox.ac.uk （場景圖、SLAM）
     - Freiburg https://rl.uni-freiburg.de （場景圖）、TUM CVG https://cvg.cit.tum.de （SLAM、3D）
     - HKU MaRS https://mars.hku.hk （LiDAR SLAM）、浙大 FAST Lab https://github.com/ZJU-FAST-Lab （規劃）
     - KAIST RaiLab https://railab.kaist.ac.kr （四足）
   - 查法：看上列頁面近期發表，或 WebSearch `<機構> <主題關鍵字> <年月>`。
1. **arXiv API 補漏**：每個主題用下表關鍵字查 `http://export.arxiv.org/api/query`，加 `submittedDate:[上次更新日 TO 今天]`，`sortBy=submittedDate`，`max_results=100`。抓不到 API 時改用 WebSearch，查詢加上年月。

   | 主題 | 分類 | 關鍵字（abs 或 ti，OR 串接） |
   |---|---|---|
   | vln | cs.RO, cs.CV | "vision-language navigation", "object goal navigation", "embodied navigation", "navigation foundation model" |
   | local-nav | cs.RO | "visual navigation" AND (diffusion OR "world model" OR "reinforcement learning"), "end-to-end navigation" |
   | semantic-map | cs.RO, cs.CV | "scene graph", "open-vocabulary map", "semantic mapping" |
   | quadruped | cs.RO | (quadruped OR legged) AND (perceptive OR navigation OR terrain) |
   | wheel-legged | cs.RO | "wheel-legged", "wheeled-legged", "legged-wheeled" |
   | slam | cs.RO, cs.CV | SLAM, "visual odometry", "LiDAR-inertial", "place recognition", relocalization |
   | perception-3d | cs.CV, cs.RO | "depth estimation", "feed-forward reconstruction", "3D reconstruction" AND (VGGT OR pointmap), occupancy |
   | vision | cs.CV | "open-vocabulary detection", "open-vocabulary segmentation", "vision foundation model" |
   | real2sim | cs.RO, cs.CV | "real-to-sim", real2sim, "digital twin" AND robot, "Gaussian splatting" AND simulation |

2. **補充來源**（WebSearch）：Science Robotics、RA-L、T-RO 新刊；當期 CoRL / RSS / ICRA / IROS / CVPR 接收論文。
3. **篩選**：每主題每次最多收 5 篇，NVIDIA 的不佔名額。名額優先給第 0 步名單內的機構，其次依：有實機實驗 > 開源程式或權重 > 標準 benchmark 上宣稱 SOTA。純 benchmark 微幅改進、只在遙測或醫療影像上驗證的不收。機構以 arXiv 摘要頁或論文首頁的作者單位為準，「機構」欄要填。
4. **確認**：收錄前 WebFetch arXiv 摘要頁，「讀到」至少是 `摘要`；抓不到摘要頁的才寫 `標題`。

## 每次更新

1. 上次更新日期看最新月報的「最後更新」。
2. 依主題加進 `topics/*.md` 的表格，新的放最上面。已收過的（以 arXiv ID 或 DOI 判斷）不重複加；有新版本或被會議／期刊接收時更新原列。
3. 在 `digests/YYYY-MM.md`（當月，沒有就建立）加一段本次新增摘要，並更新「最後更新」日期。新月報要有「## 趨勢」段落，README 會抓它。
4. 跑 `python3 scripts/build_readme.py` 重新產生 README。README 是產生的，不要手改。
5. 開新 branch `update/YYYY-MM-DD`，commit，開 PR 到 main；不直接推 main。沒有新論文就不開 PR。

## 檔案格式

- `topics/*.md` 固定兩段：`## 在解決的問題`（條列）與 `## 最新論文`（表格）。新論文只加在「最新論文」表。
- 經典論文放 `data/classics.csv`，不放主題檔；同一篇不要同時出現在兩處。
- 每月第一次更新時跑 `python3 scripts/fetch_metrics.py` 刷新引用數與 star，並把「最新論文」中發表滿一年、且引用 ≥ 300 或 star ≥ 1k 的論文移到 `classics.csv`（從主題檔刪除該列）。
- 「在解決的問題」只在領域出現新的主要問題或舊問題被解決時改。

## 表格欄位

`| 日期 | 論文 | 機構 | 重點 | 數據 | 讀到 |`

- 日期：arXiv 首次提交或正式發表的年月。
- 重點：一句話講方法上和前作不同之處，不抄摘要。
- 數據：作者自報的關鍵數字（benchmark + 數值）；沒看到就留空，不要猜。
- 讀到：`全文` / `摘要` / `標題`，照實寫實際讀到的程度。只看到標題的不寫方法細節。

## 月報

- 每月一檔。開頭寫本月趨勢 2–4 點（觀察到的寫「觀察」，沒驗證的推論寫「推測」）。
- 之後列本月新增論文，連到對應主題檔。

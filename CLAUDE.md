# Robot Nav Survey

- 加論文、擴充重要論文、新增主題時，先用 Skill 工具呼叫 `update-survey`（`.claude/skills/update-survey/`）。
- README 由 `scripts/build_readme.py` 產生，改 `topics/`、`data/`、`digests/` 後重跑，不手改 README。
- 一律用繁體中文（台灣用語）；commit message 用英文、conventional 前綴（`docs: ...`）。
- 範圍：AMR（輪式）、四足、輪足的導航，以及機器人用得到的視覺、3D 感知、SLAM、Real2Sim。純操作（manipulation）、純人形全身控制、純自駕不收，除非方法可直接用在上述機體。

## 主題邊界

一篇只放一個主題，以主要貢獻判斷：

- `vln.md`：用語言或高階目標下指令的導航，含導航基礎模型、VLA。
- `local-nav.md`：不靠語言或語意目標的導航：從感測器到軌跡或速度的策略（diffusion、world model、RL）、幾何探索與路徑規劃、社交導航。
- `quadruped.md` / `wheel-legged.md`：該機體特有的運動控制與導航。
- `slam.md`：SLAM、VO、LIO、重定位、回環。
- `reconstruction.md`：feed-forward 3D 重建、SfM、3DGS／NeRF 表示與渲染；產出是幾何與外觀。以軌跡或 ATE 為主要評估的線上追蹤放 slam；產出要能拿來模擬、訓練或評估策略（碰撞、物理、可互動物件）的放 real2sim。
- `perception-3d.md`：單目與雙目深度估計、occupancy。
- `semantic-map.md`：給導航查詢用的語意地圖、場景圖。
- `spatial.md`：3D 偵測、3D 實例分割、3D grounding、空間推理 VLM 與其 benchmark。以單一場景的理解為主；要累積成給導航查詢的地圖才放 semantic-map。純自駕的室外 LiDAR／BEV 偵測不收。
- `vision.md`：2D 偵測、分割、追蹤、視覺基礎模型。
- `real2sim.md`：模擬器與具身場景資料集、當模擬器用的 world model，以及把真實場景重建成可模擬、可訓練或可評估策略的環境。拿來當規劃器的 world model 歸它服務的導航主題。

# 3D 場景重建（feed-forward、SfM、3DGS／NeRF）

## 在解決的問題

- feed-forward 重建：不跑 SfM 優化，一次前向得到相機與幾何；挑戰在大規模與串流輸入。
- 傳統 SfM 的速度與穩健度：全域最佳化、位姿圖初始化。
- 3D 表示：3DGS 取代 NeRF，可即時渲染；表面品質與無位姿輸入仍在改進。
- 動態場景：同時重建幾何、運動與相機。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-04 | [Feed-forward 3D scene modeling survey](https://arxiv.org/abs/2604.14025) · [專案頁](https://ff3d-survey.github.io) | Zhejiang / NTU / Monash / ETH / Tübingen | feed-forward 3D 重建綜述，涵蓋 Point3R、IncVGGT、ZipMap 等串流／增量版本 |  | [GitHub](https://github.com/ziplab/Awesome-Feed-Forward-3D) | arXiv |
| 2026-02 | [VGG-T³](https://arxiv.org/abs/2602.23361) · [專案頁](https://research.nvidia.com/labs/dvl/projects/vgg-ttt) | NVIDIA / Toronto | 大規模離線 feed-forward 重建 |  | [GitHub](https://github.com/nv-dvl/vgg-ttt) | CVPR 2026 |
| 2025-11 | [AMB3R](https://arxiv.org/abs/2511.20343) · [專案頁](https://hengyiwang.github.io/projects/amber) | UCL | feed-forward 公制尺度重建 + 稀疏體素後端，不微調即可延伸到 VO／SLAM |  | [GitHub](https://github.com/HengyiWang/amb3r) | CVPR 2026 |

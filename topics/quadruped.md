# 四足

## 在解決的問題

- 感知不可靠時仍要穩（反光、草叢、高度圖雜訊）：融合外部感知與本體感知。
- sim-to-real：大規模平行模擬 + domain randomization + 特權教師蒸餾。
- 敏捷技能（跑酷、跳躍、越溝）與技能切換。
- 從「跟隨速度指令」走向「運動與導航一體」，直接走到目標。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 來源 |
|---|---|---|---|---|---|
| 2026-07 | [APT-RL: Agile perceptive multi-skill locomotion](https://arxiv.org/abs/2607.13579) | KAIST 等 | 軌跡最佳化 8 分鐘產生 18 萬條動作先驗，再用 RL + 機載感知適應 3D 地形 | 單一策略過樓梯／欄／踏石／溝；瞬間最高 6 m/s | Science Robotics 2026 |
| 2026-06 | [Perceptive Platform Adaptive Locomotion](https://arxiv.org/abs/2606.25179) | Oxford DRS | 感知只給 critic，感知有雜訊時比完全感知策略穩 |  | arXiv |
| 2026-06 | [GUIDE](https://arxiv.org/abs/2606.10832) | Zhejiang / TeleAI / Oxford 等 | 端到端腿式導航 |  | arXiv |
| 2026-04 | [HiPAN](https://arxiv.org/abs/2604.26504) | KAIST | 非結構 3D 環境的姿態自適應分層導航 |  | RA-L 2026 |

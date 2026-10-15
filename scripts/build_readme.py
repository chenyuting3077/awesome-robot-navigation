#!/usr/bin/env python3
"""把 topics/*.md、data/classics.csv（+ metrics.json）與最新月報組成一頁到底的 README.md。

topics/ 與 data/ 是資料來源，README 由本腳本產生，不要手改。
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = [
    "vln", "local-nav", "semantic-map", "quadruped", "wheel-legged",
    "slam", "perception-3d", "vision", "real2sim",
]

# 分級門檻：(名稱, 引用數, star 數)，任一達標即可
TIERS = [("奠基", 1000, 10000), ("主流", 300, 1000)]

HEADER = """# Robot Nav Survey

AMR、四足、輪足機器人的導航、視覺、3D 感知、SLAM 與 Real2Sim 前沿論文整理，每三天自動更新。

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 或 digests/ 後重跑 -->

- 每三天由排程 agent 依 [CLAUDE.md](CLAUDE.md) 的規則搜尋新論文並開 PR，審過再 merge。
- 手動更新：在 repo 裡開 Claude Code，說「更新論文整理」。
- 每個主題分三段：在解決的問題、經典（近五年，依引用與 star 分級）、最新論文。
- 分級：**奠基** 引用 ≥ 1000 或 star ≥ 10k；**主流** 引用 ≥ 300 或 star ≥ 1k；其餘為**新興**。引用來自 Semantic Scholar，star 來自 GitHub。「年」是 arXiv 首次公開年份，「來源」是正式刊登的會議或期刊。
- 程式碼標「未公開」：論文頁、arXiv 頁與 GitHub 搜尋都找不到作者釋出的官方程式碼（第三方重現不算）。

## 定期追蹤的來源

完整查法與關鍵字見 [CLAUDE.md](CLAUDE.md#搜尋方式)。

- **NVIDIA Research**（每次必查）：[Robotics](https://research.nvidia.com/research-area/robotics)、[Computer Vision](https://research.nvidia.com/research-area/computer-vision)、[Seattle Robotics Lab](https://research.nvidia.com/labs/srl)、[GEAR](https://research.nvidia.com/labs/gear/)、[NVlabs GitHub](https://github.com/NVlabs)
- **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics
- **實驗室**：[ETH RSL](https://rsl.ethz.ch)、[ETH ASL](https://asl.ethz.ch)、[MIT SPARK](https://web.mit.edu/sparklab/)、[CMU AirLab](https://theairlab.org)、[Berkeley RAIL](https://rail.eecs.berkeley.edu)、[UCSD Xiaolong Wang](https://xiaolonw.github.io)、[PKU EPIC](https://pku-epic.github.io)、[InternRobotics](https://github.com/InternRobotics)、[Oxford VGG](https://www.robots.ox.ac.uk/~vgg/)、[Oxford DRS](https://dynamic.robots.ox.ac.uk)、[Freiburg](https://rl.uni-freiburg.de)、[TUM CVG](https://cvg.cit.tum.de)、[HKU MaRS](https://mars.hku.hk)、[ZJU FAST Lab](https://github.com/ZJU-FAST-Lab)、[KAIST RaiLab](https://railab.kaist.ac.kr)
- **arXiv**：cs.RO、cs.CV，依主題關鍵字查上次更新後的新投稿
- **期刊**：Science Robotics、RA-L、T-RO
- **會議**：CoRL、RSS、ICRA、IROS、CVPR（接收論文公布時）
"""


def anchor(title: str) -> str:
    # GitHub 標題錨點：小寫、去標點、空白轉 -
    s = re.sub(r"[^\w\- ]", "", title.lower(), flags=re.UNICODE)
    return s.replace(" ", "-")


def tier(cites: int, stars: int) -> str:
    for name, c, s in TIERS:
        if cites >= c or stars >= s:
            return name
    return "新興"


def classics_table(rows, metrics) -> str:
    items = []
    for r in rows:
        p = metrics["papers"].get(r["arxiv"]) or {}
        cites = p.get("citationCount") or 0
        year = p.get("year") or int("20" + r["arxiv"][:2])
        stars = metrics["stars"].get(r["repo"]) or 0
        items.append((r, year, cites, stars, tier(cites, stars)))
    order = {"奠基": 0, "主流": 1, "新興": 2}
    items.sort(key=lambda x: (order[x[4]], -x[2]))

    lines = ["| 分級 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |", "|---|---|---|---|---|---|---|---|"]
    for r, year, cites, stars, t in items:
        paper = f"[{r['name']}](https://arxiv.org/abs/{r['arxiv']})"
        if r["project"]:
            paper += f" · [專案頁]({r['project']})"
        star = f"[{stars:,}](https://github.com/{r['repo']})" if r["repo"] else "未公開"
        lines.append(f"| {t} | {year} | {paper} | {r['org']} | {r['note']} | {r['venue']} | {cites:,} | {star} |")
    return "\n".join(lines)


def main() -> None:
    classics = list(csv.DictReader((ROOT / "data" / "classics.csv").open()))
    metrics = json.loads((ROOT / "data" / "metrics.json").read_text())

    sections = []
    for name in TOPICS:
        text = (ROOT / "topics" / f"{name}.md").read_text().strip()
        title, body = text.split("\n", 1)
        problems, latest = body.split("## 最新論文", 1)
        problems = problems.replace("## 在解決的問題", "").strip()
        rows = [r for r in classics if r["topic"] == name]
        parts = [f"## {title.lstrip('# ').strip()}", "### 在解決的問題", problems]
        if rows:
            parts += [f"### 經典（近五年，資料日期 {metrics['fetched']}）", classics_table(rows, metrics)]
        parts += ["### 最新論文", latest.strip()]
        sections.append((title.lstrip("# ").strip(), "\n\n".join(parts)))

    digests = sorted((ROOT / "digests").glob("*.md"), reverse=True)
    latest = digests[0].read_text()
    trend = latest.split("## 趨勢", 1)[1].split("\n## ", 1)[0].strip()
    updated = re.search(r"最後更新：(\S+)", latest).group(1)

    out = [HEADER, f"最後更新：{updated}\n", "## 目錄\n"]
    out.append(f"- [本月趨勢（{digests[0].stem}）](#本月趨勢{anchor(digests[0].stem)})")
    out += [f"- [{t}](#{anchor(t)})" for t, _ in sections]
    out.append("- [月報](#月報)\n")
    out.append(f"## 本月趨勢（{digests[0].stem}）\n\n{trend}\n")
    out += [f"{s}\n" for _, s in sections]
    out.append("## 月報\n")
    out += [f"- [{d.stem}](digests/{d.name})" for d in digests]

    (ROOT / "README.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""把 topics/*.md 與最新月報組成一頁到底的 README.md。

topics/ 是唯一資料來源，README 由本腳本產生，不要手改。
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = [
    "vln", "local-nav", "semantic-map", "quadruped", "wheel-legged",
    "slam", "perception-3d", "vision", "real2sim",
]

HEADER = """# Robot Nav Survey

AMR、四足、輪足機器人的導航、視覺、3D 感知、SLAM 與 Real2Sim 前沿論文整理，每週自動更新。

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/ 或 digests/ 後重跑 -->

- 每週由排程 agent 依 [CLAUDE.md](CLAUDE.md) 的規則搜尋新論文並開 PR，審過再 merge。
- 手動更新：在 repo 裡開 Claude Code，說「更新論文整理」。
"""


def anchor(title: str) -> str:
    # GitHub 標題錨點：小寫、去標點、空白轉 -
    s = re.sub(r"[^\w\- ]", "", title.lower(), flags=re.UNICODE)
    return s.replace(" ", "-")


def main() -> None:
    sections = []
    for name in TOPICS:
        lines = (ROOT / "topics" / f"{name}.md").read_text().strip().splitlines()
        title = lines[0].lstrip("# ").strip()
        body = "\n".join(lines[1:]).strip()
        sections.append((title, body))

    digests = sorted((ROOT / "digests").glob("*.md"), reverse=True)
    latest = digests[0]
    trend = latest.read_text().split("## 趨勢", 1)[1].split("\n## ", 1)[0].strip()
    updated = re.search(r"最後更新：(\S+)", latest.read_text()).group(1)

    out = [HEADER, f"最後更新：{updated}\n", "## 目錄\n"]
    out.append(f"- [本月趨勢（{latest.stem}）](#本月趨勢{anchor(latest.stem)})")
    out += [f"- [{t}](#{anchor(t)})" for t, _ in sections]
    out.append("- [月報](#月報)\n")
    out.append(f"## 本月趨勢（{latest.stem}）\n\n{trend}\n")
    out += [f"## {t}\n\n{b}\n" for t, b in sections]
    out.append("## 月報\n")
    out += [f"- [{d.stem}](digests/{d.name})" for d in digests]

    (ROOT / "README.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

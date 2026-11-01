#!/usr/bin/env python3
"""依 README「怎樣算重要論文」的封存規則，把 data/classics.csv 的論文移到 data/archive.csv。

  python3 scripts/prune.py        只列出會封存的論文
  python3 scripts/prune.py --apply

分數用相加而不是取大值：取大值時，引用與 star 都中等的論文會排在只有單項剛過門檻的論文後面。
引用先除以年份門檻，否則舊論文一定贏過新論文。
"""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_readme import ROOT, STAR_BAR, paper_stats, tier  # noqa: E402
from harvest import THRESHOLD  # noqa: E402

CAP = 30  # 2026-11 試算：受保護論文讓電腦視覺、3D 重建略超過 30
LOW = 100  # 規則一的引用與 star 門檻
GRACE = 2  # 公開滿幾個年度才適用規則一
KEEP = {"推薦", "基準", "知名"}
UNCAPPED = "知名"  # 只佔主頁、不佔名額；算進上限的話，移回一篇就會多擠掉一篇
STALE = "新興滿兩年未達門檻"
OVER = "超過主題上限"


def main() -> None:
    apply = "--apply" in sys.argv
    path, archive_path = ROOT / "data" / "classics.csv", ROOT / "data" / "archive.csv"
    rows = list(csv.DictReader(path.open()))
    metrics = json.loads((ROOT / "data" / "metrics.json").read_text())
    now = int(metrics["fetched"][:4])

    moved = {}
    for r in rows:
        year, cites, stars = paper_stats(r, metrics)
        if set(r["tags"].split(";")) & KEEP or not year:
            continue
        if tier(year, cites, stars) == "新興" and year <= now - GRACE and cites < LOW and stars < LOW:
            moved[id(r)] = STALE

    capped = [r for r in rows if id(r) not in moved and UNCAPPED not in r["tags"].split(";")]
    for topic, n in Counter(r["topic"] for r in capped).items():
        pool = []
        for r in rows:
            if r["topic"] != topic or id(r) in moved or set(r["tags"].split(";")) & KEEP:
                continue
            year, cites, stars = paper_stats(r, metrics)
            if year in THRESHOLD and tier(year, cites, stars) != "奠基":
                pool.append((cites / THRESHOLD[year] + stars / STAR_BAR, r))
        pool.sort(key=lambda x: x[0])
        for score, r in pool[:max(0, n - CAP)]:
            moved[id(r)] = OVER

    for r in rows:
        if id(r) in moved:
            year, cites, stars = paper_stats(r, metrics)
            print(f"{moved[id(r)]}\t{r['topic']}\t{r['name']}\t{year}\t引用 {cites}\tstar {stars}\t{r['tags']}")
    print(f"共 {len(moved)} 篇，{Counter(moved.values())}")
    if not apply:
        return

    fields = list(rows[0])
    old = list(csv.DictReader(archive_path.open())) if archive_path.exists() else []
    with archive_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fields + ["reason"], lineterminator="\n")
        w.writeheader()
        w.writerows(old + [{**r, "reason": moved[id(r)]} for r in rows if id(r) in moved])
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fields, lineterminator="\n")
        w.writeheader()
        w.writerows(r for r in rows if id(r) not in moved)


if __name__ == "__main__":
    main()

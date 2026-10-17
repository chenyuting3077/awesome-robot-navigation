#!/usr/bin/env python3
"""檢查 topics/*.md 與 data/classics.csv 的格式，有錯就以非零結束；build_readme.py 會先跑它。

只檢查機械式規則。曾發生過的錯：改欄位時空白格被吃掉，「來源」錯位到「數據」欄；
機構留空；沒有官方程式碼卻沒標「未公開」。
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAGS = {"獲獎", "基準", "機構", "推薦"}
COLS = 7  # | 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
ARXIV = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")


def check_topics(topics, errors):
    seen = {}
    for name in topics:
        path = ROOT / "topics" / f"{name}.md"
        text = path.read_text()
        if "## 在解決的問題" not in text or "## 最新論文" not in text:
            errors.append(f"{path.name}：缺「## 在解決的問題」或「## 最新論文」")
            continue
        table = text.split("## 最新論文", 1)[1]
        for n, line in enumerate(table.splitlines(), 1):
            if not line.startswith("|") or line.startswith("| 日期") or line.startswith("| ---"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            where = f"{path.name}「最新論文」第 {n} 行"
            if len(cells) != COLS:
                errors.append(f"{where}：{len(cells)} 欄，應為 {COLS} 欄")
                continue
            date, paper, org, note, data, code, venue = cells
            if not re.fullmatch(r"\d{4}-\d{2}", date):
                errors.append(f"{where}：日期「{date}」不是 YYYY-MM")
            for label, v in (("論文", paper), ("機構", org), ("重點", note), ("來源", venue)):
                if not v:
                    errors.append(f"{where}：{label}欄空白")
            if data == venue or data.lower() == "arxiv":
                errors.append(f"{where}：數據欄是「{data}」，像是來源錯位")
            if not (code == "未公開" or code.startswith("[GitHub](")):
                errors.append(f"{where}：程式碼欄應為 [GitHub](...) 或「未公開」，現在是「{code}」")
            if m := ARXIV.search(paper):
                seen[m.group(1)] = where
    return seen


def check_classics(topics, in_topics, errors):
    ids = {}
    for n, r in enumerate(csv.DictReader((ROOT / "data" / "classics.csv").open()), 2):
        where = f"classics.csv 第 {n} 行（{r['name']}）"
        if r["topic"] not in topics:
            errors.append(f"{where}：topic「{r['topic']}」不在 TOPICS")
        for col in ("name", "org", "venue", "note"):
            if not r[col].strip():
                errors.append(f"{where}：{col} 空白")
        if not r["id"] and not r["url"]:
            errors.append(f"{where}：id 與 url 都空白")
        if r["id"]:
            if not (re.fullmatch(r"\d{4}\.\d{4,5}", r["id"]) or r["id"].startswith("DOI:")):
                errors.append(f"{where}：id「{r['id']}」不是 arXiv 編號或 DOI:...")
            if r["id"] in ids:
                errors.append(f"{where}：id 與第 {ids[r['id']]} 行重複")
            ids[r["id"]] = n
            if r["id"] in in_topics:
                errors.append(f"{where}：同時出現在 {in_topics[r['id']]}")
        if r["repo"] and not re.fullmatch(r"[\w.-]+/[\w.-]+", r["repo"]):
            errors.append(f"{where}：repo「{r['repo']}」不是 owner/name")
        if bad := {t for t in r["tags"].split(";") if t} - TAGS:
            errors.append(f"{where}：tags 只能用 {'、'.join(sorted(TAGS))}，不能用 {'、'.join(sorted(bad))}")
        if "機構" in r["tags"].split(";") and not r["repo"]:
            errors.append(f"{where}：tag「機構」要求開源，但 repo 空白")


def check(topics) -> list[str]:
    errors = []
    in_topics = check_topics(topics, errors)
    check_classics(topics, in_topics, errors)
    return errors


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from build_readme import TOPICS

    errs = check(TOPICS)
    print("\n".join(errs) or "OK")
    sys.exit(1 if errs else 0)

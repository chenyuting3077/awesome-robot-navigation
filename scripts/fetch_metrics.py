#!/usr/bin/env python3
"""抓 data/classics.csv 每篇的引用數（Semantic Scholar）與 GitHub star，存到 data/metrics.json。

Semantic Scholar 未登入時共用限流，常回 429，所以用指數退避重試；
有 S2_API_KEY 環境變數就帶上。GitHub 優先用 gh CLI（已登入，限額高），沒有就用
GITHUB_TOKEN 或匿名 API（每小時 60 次，約夠一輪）。
"""
import csv
import datetime
import json
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
S2_URL = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,year,venue,citationCount"


def request_json(req: urllib.request.Request, tries: int = 8):
    # 429、5xx、逾時與斷線都重試；HF API 偶爾讀取逾時，S2 未登入常回 429
    for i in range(tries):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if (e.code != 429 and e.code < 500) or i == tries - 1:
                raise
        except (TimeoutError, urllib.error.URLError):
            if i == tries - 1:
                raise
        time.sleep(min(2 ** i, 60))


def s2_id(pid: str) -> str:
    # classics.csv 的 id：arXiv 編號，或 `DOI:...`
    return pid if pid.startswith("DOI:") else f"ARXIV:{pid}"


def fetch_papers(ids):
    headers = {"Content-Type": "application/json"}
    if key := os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = key
    body = json.dumps({"ids": [s2_id(i) for i in ids]}).encode()
    res = request_json(urllib.request.Request(S2_URL, data=body, headers=headers))
    return {
        i: (None if p is None else {k: p[k] for k in ("title", "year", "venue", "citationCount")})
        for i, p in zip(ids, res)
    }


def fetch_stars(repo):
    if shutil.which("gh"):
        out = subprocess.run(["gh", "api", f"repos/{repo}", "--jq", ".stargazers_count"],
                             capture_output=True, text=True)
        return int(out.stdout) if out.returncode == 0 else None
    headers = {"Accept": "application/vnd.github+json"}
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    try:
        return request_json(urllib.request.Request(f"https://api.github.com/repos/{repo}",
                                                   headers=headers))["stargazers_count"]
    except urllib.error.HTTPError:
        return None


def fetch_hf_upvotes(aid):
    # Hugging Face Papers 的按讚數；沒收錄的論文回 None（多半是 2023 年前或冷門的）
    try:
        p = request_json(urllib.request.Request(f"https://huggingface.co/api/papers/{aid}"))
        return p.get("upvotes")
    except urllib.error.HTTPError:
        return None


def main():
    rows = list(csv.DictReader((ROOT / "data" / "classics.csv").open()))
    ids = [r["id"] for r in rows if r["id"]]  # 沒有 id 的（部落格、技術報告）不查引用
    papers = fetch_papers(ids)
    repos = sorted({r["repo"] for r in rows if r["repo"]})
    stars = {repo: fetch_stars(repo) for repo in repos}
    hf = {}
    for i in ids:
        if not i.startswith("DOI:"):
            hf[i] = fetch_hf_upvotes(i)
            time.sleep(0.3)
    out = {"fetched": datetime.date.today().isoformat(), "papers": papers, "stars": stars, "hf": hf}
    (ROOT / "data" / "metrics.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    for i in ids:
        if papers[i] is None:
            print(f"找不到：{i}")
    for repo, s in stars.items():
        if s is None:
            print(f"抓不到 star：{repo}")


if __name__ == "__main__":
    main()

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
    for i in range(tries):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == tries - 1:
                raise
            time.sleep(2 ** i)


def fetch_papers(arxiv_ids):
    headers = {"Content-Type": "application/json"}
    if key := os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = key
    body = json.dumps({"ids": [f"ARXIV:{a}" for a in arxiv_ids]}).encode()
    res = request_json(urllib.request.Request(S2_URL, data=body, headers=headers))
    return {
        a: (None if p is None else {k: p[k] for k in ("title", "year", "venue", "citationCount")})
        for a, p in zip(arxiv_ids, res)
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


def main():
    rows = list(csv.DictReader((ROOT / "data" / "classics.csv").open()))
    papers = fetch_papers([r["arxiv"] for r in rows])
    repos = sorted({r["repo"] for r in rows if r["repo"]})
    stars = {repo: fetch_stars(repo) for repo in repos}
    out = {"fetched": datetime.date.today().isoformat(), "papers": papers, "stars": stars}
    (ROOT / "data" / "metrics.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    for r in rows:
        if papers[r["arxiv"]] is None:
            print(f"找不到：{r['arxiv']} {r['name']}")
    for repo, s in stars.items():
        if s is None:
            print(f"抓不到 star：{repo}")


if __name__ == "__main__":
    main()

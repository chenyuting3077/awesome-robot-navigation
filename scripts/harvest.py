#!/usr/bin/env python3
"""用 Semantic Scholar 依主題關鍵字撈高引用候選論文，寫到 data/candidates.json。

只做「引用門檻」這一條的初篩；相關性與其他收錄條件（獲獎、基準、機構、推薦）
要人工判斷後寫進 data/classics.csv。門檻依年份調整，因為新論文引用還沒累積。
"""
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "title,year,citationCount,venue,externalIds"

# 年份 -> 最低引用數；2026 年起的論文不看引用（太新），靠其他條件收錄
THRESHOLD = {2021: 300, 2022: 300, 2023: 150, 2024: 80, 2025: 30}

QUERIES = {
    "vln": ['"vision-and-language navigation"', '"vision-language navigation"', '"object goal navigation"',
            '"object navigation"', '"embodied navigation"', '"language-guided navigation"',
            '"zero-shot navigation"', '"instruction following" navigation robot'],
    "local-nav": ['"visual navigation"', '"navigation foundation model"', '"end-to-end navigation"',
                  '"local planner"', '"navigation policy"', '"autonomous exploration"', '"social navigation"',
                  '"robot navigation" learning'],
    "semantic-map": ['"3D scene graph"', '"open-vocabulary 3D"', '"semantic mapping"', '"open-vocabulary map"',
                     '"language embedded"', '"open-set" mapping'],
    "quadruped": ['quadruped', '"legged robot"', '"legged locomotion"', '"quadrupedal"'],
    "wheel-legged": ['"wheel-legged"', '"wheeled-legged"', '"legged-wheeled"', '"wheeled bipedal"'],
    "slam": ['SLAM', '"visual odometry"', '"lidar odometry"', '"lidar-inertial"', '"visual-inertial"',
             '"place recognition"', '"loop closure"', '"bundle adjustment"'],
    "perception-3d": ['"depth estimation"', '"stereo matching"', '"multi-view stereo"', '"3D reconstruction"',
                      '"gaussian splatting"', '"occupancy prediction"', 'pointmap', '"novel view synthesis"'],
    "vision": ['"open-vocabulary detection"', '"open-vocabulary segmentation"', '"open-vocabulary object detection"',
               '"segment anything"', '"vision foundation model"', '"self-supervised" visual representation',
               '"feature matching"', '"point tracking"', '"real-time object detection"'],
    "real2sim": ['"real-to-sim"', 'real2sim', '"digital twin" robot', '"sim-to-real"', '"robot simulation"',
                 '"gaussian splatting" simulation robot', '"world model" robot'],
}


def search(query: str):
    headers = {}
    if key := os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = key
    params = {"query": query, "year": "2021-", "minCitationCount": 30,
              "sort": "citationCount:desc", "fields": FIELDS, "fieldsOfStudy": "Computer Science"}
    token = None
    while True:
        if token:
            params["token"] = token
        url = f"{URL}?{urllib.parse.urlencode(params)}"
        # 未登入時與所有匿名使用者共用限額，429 很常見，退避上限拉到 60 秒
        for i in range(15):
            try:
                res = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60))
                break
            except urllib.error.HTTPError as e:
                if e.code != 429 or i == 14:
                    raise
                time.sleep(min(2 ** i, 60))
        yield from res.get("data", [])
        token = res.get("token")
        if not token:
            return
        time.sleep(3)


def main():
    path = ROOT / "data" / "candidates.json"
    out = json.loads(path.read_text()) if path.exists() else {}
    for topic, queries in QUERIES.items():
        if topic in out:  # 中斷後重跑時跳過已完成的主題；要全部重撈就先刪檔
            continue
        found = {}
        for q in queries:
            for p in search(q):
                year, cites = p.get("year"), p.get("citationCount") or 0
                if year is None or cites < THRESHOLD.get(year, 10**9):
                    continue
                aid = (p.get("externalIds") or {}).get("ArXiv")
                key = aid or p["paperId"]
                found[key] = {"arxiv": aid, "doi": (p.get("externalIds") or {}).get("DOI"), "title": p["title"], "year": year,
                              "citations": cites, "venue": p.get("venue") or ""}
            time.sleep(3)
        out[topic] = sorted(found.values(), key=lambda x: -x["citations"])
        path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
        print(f"{topic}: {len(out[topic])} 篇", flush=True)


if __name__ == "__main__":
    main()

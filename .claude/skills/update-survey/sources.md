# 新論文的搜尋來源

改動來源清單時，同步改 `scripts/build_readme.py` 裡 README 的「定期追蹤的來源」。

0. **先查重點來源**（最優先）：arXiv API 無法依機構篩選，所以先逐一查下列來源的近期發表，再做第 1 步。
   - **NVIDIA**（每次都要查）：
     - https://research.nvidia.com/research-area/robotics 、 https://research.nvidia.com/research-area/computer-vision ：依年份列出論文，只顯示年份，月份看論文網址 slug。網站常比 arXiv 晚上架，所以兩邊都要查。
     - https://research.nvidia.com/publications ：全部論文，`?page=N` 翻頁，只能依會議篩選（例如 CoRL `?f%5B0%5D=publication_events%3A35`），不能依領域篩選。
     - 實驗室：Seattle Robotics Lab https://research.nvidia.com/labs/srl 、GEAR https://research.nvidia.com/labs/gear/ 。
     - 程式碼：https://github.com/NVlabs 。
     - 再用 WebSearch `NVIDIA <主題關鍵字> <年月>` 補查 Isaac、Cosmos、GR00T 等產品線的技術報告。
     - research.nvidia.com/labs/ 首頁會擋爬蟲（403），直接用上面的子頁。
   - **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba（AMAP、DAMO）、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics；另 Waymo、Sony AI、Adobe、Samsung、Baidu、Microsoft、Apple的研究單位也算名單內（不必每次查）。
   - **實驗室**（括號內為主要相關主題）：
     - ETH RSL https://rsl.ethz.ch （四足、輪足）、ETH ASL https://asl.ethz.ch （SLAM、導航）
     - MIT SPARK https://web.mit.edu/sparklab/ （SLAM、場景圖）
     - CMU AirLab https://theairlab.org （SLAM、導航）
     - Berkeley RAIL https://rail.eecs.berkeley.edu （導航基礎模型）
     - UCSD Xiaolong Wang https://xiaolonw.github.io （腿式 VLA）
     - PKU EPIC https://pku-epic.github.io （VLN）
     - 上海 AI Lab InternRobotics https://github.com/InternRobotics （局部導航）
     - Oxford VGG https://www.robots.ox.ac.uk/~vgg/ （3D 重建）、Oxford DRS https://dynamic.robots.ox.ac.uk （場景圖、SLAM）
     - Freiburg https://rl.uni-freiburg.de （場景圖）、TUM CVG https://cvg.cit.tum.de （SLAM、3D）
     - HKU MaRS https://mars.hku.hk （LiDAR SLAM）、浙大 FAST Lab https://github.com/ZJU-FAST-Lab （規劃）
     - KAIST RaiLab https://railab.kaist.ac.kr （四足）
   - **擴充追蹤名單**（只用來找論文，不放寬收錄資格，也不適用 `機構` 標籤；不必每次查）：
     - 韓國：KAIST Urban Robotics Lab https://github.com/url-kaist （LiDAR、SLAM）、SPARO Lab https://github.com/sparolab （LiDAR、SLAM）
     - 企業：Ultralytics https://github.com/ultralytics 、Galbot https://github.com/GalaxyGeneralRobotics 、Agibot https://github.com/AgibotTech 、DeepRobotics https://github.com/DeepRoboticsLab 、Xiaomi Robotics https://github.com/XiaomiRobotics 、Insta360 Research https://github.com/Insta360-Research-Team 、Robbyant https://github.com/robbyant
     - HKUST Aerial Robotics https://uav.hkust.edu.hk/ （SLAM、規劃）、OpenDriveLab https://opendrivelab.com （端到端、資料集，偏自駕，純自駕不收）、CUHK LaVi Lab https://github.com/LaVi-Lab （3D 空間理解）
     - ZJU3DV https://github.com/zju3dv （3D 視覺、重建）、SYSU STAR https://robotics-star.com/ （導航、規劃）、清華 AIR Discover Lab https://github.com/AIR-DISCOVER （模擬、導航）、CUHK 深圳 GAP-LAB https://gaplab.cuhk.edu.cn/ （3D 重建）、HIT nROS-Lab https://github.com/HITSZ-NRSL （SLAM）
     - 中國：清華 TEA Lab https://github.com/TEA-Lab （具身智慧）、清華 MARS Lab https://github.com/Tsinghua-MARS-Lab （感知、地圖，偏自駕）、清華 THU-MIG https://github.com/THU-MIG （即時偵測）、清華 ISRLab https://github.com/Tsinghua-ISRLab （足式、機器人學習）、上海交大 IRMV http://irmv.sjtu.edu.cn/ （SLAM、機器人視覺）、上海交大 MVIG https://github.com/mvig-sjtu （視覺、機器人）、上海交大 ViSYS https://sjtu-visys.github.io/ （SLAM、資料集）、上海交大 AutoLab https://github.com/AutoLab-SAI-SJTU （導航、3D 重建）、浙大 APRIL https://github.com/APRIL-ZJU （LiDAR、SLAM）、浙大 Robotics Lab https://github.com/ZJU-Robotics-Lab （導航、地圖）、華中科大 HUST Vision Lab https://hustvl.github.io/ （3D 視覺、偵測）、復旦 MAGIC Lab https://github.com/Fudan-MAGIC-Lab （SLAM）、北航 VRCG https://github.com/buaavrcg （3D 表示）、南大 3DV https://nju-3dv.github.io （3D 重建）、南開 MCG https://github.com/MCG-NKU （視覺基礎模型）、CASIA IVA https://github.com/CASIA-IVA-Lab （分割、視覺）、BAAI Vision https://github.com/baaivision （視覺基礎模型）、BIGAI https://github.com/bigai-ai （具身智慧、模擬）
     - 香港：HKUST SAIL https://github.com/HKUST-SAIL （3DGS、3D 重建）、HKUST RAM-LAB https://ram-lab.com/ （SLAM、感知）、HKUST (GZ) 3DAgentWorld https://github.com/3DAgentWorld （SLAM、3DGS）、CUHK MMLab https://mmlab.ie.cuhk.edu.hk/ （視覺）
     - 韓國：POSTECH CVLab https://github.com/POSTECH-CVLab （點雲、3D 視覺）、KAIST AMI https://github.com/kaist-ami （3D 語意）
     - 新加坡：NTU ARIS https://github.com/ntu-aris （SLAM、資料集）、NTU MARS Lab https://www.ntu.edu.sg/rrc/robotics-research-centre-groups/mars-lab （具身智慧）
     - 中國：復旦 Zhang Vision Group https://github.com/fudan-zvg （SPAR）、西安交大 MIV https://github.com/MIV-XJTU （JanusVLN）、中山大學 RAPID Lab https://github.com/SYSU-RoboticsLab （NaviDiffusor）、同濟感知組 https://github.com/tjiiv-cprg （EPro-PnP）、IDEA Research https://github.com/IDEA-Research （Grounding DINO）
     - 香港：HKU MMLab https://mmlab.hk/ （LLaVA-3D）
     - 歐洲：Zaragoza SLAMLab https://github.com/UZ-SLAMLab （ORB-SLAM3）、Inria GraphDeco https://team.inria.fr/graphdeco/ （3D Gaussian Splatting）、Imperial Dyson Robotics Lab https://www.imperial.ac.uk/dyson-robotics-lab/ （Gaussian Splatting SLAM、MASt3R-SLAM）、ETH PRS https://prs.igp.ethz.ch （Marigold）、ETH VIS https://github.com/SysCV （HQ-SAM）、Tübingen AVG https://github.com/autonomousvision （UniMatch）、NAVER LABS Europe https://europe.naverlabs.com/ （DUSt3R）
     - 北美：UCSD Hao Su Lab https://github.com/haosulab （ManiSkill3）、Stanford REAL https://real.stanford.edu/ （CoW）、Stanford Gradient Spaces https://gradientspaces.stanford.edu/ （WildGS-SLAM）、UMich SLED https://sled.eecs.umich.edu/ （LLM-Grounder）、UMass Embodied AGI https://embodied-agi.cs.umass.edu/ （3D-Mem）、MIT Improbable AI https://github.com/Improbable-AI （Walk These Ways）、Berkeley Hybrid Robotics https://hybrid-robotics.berkeley.edu/ （DiffuseLoco）、SAIR Lab https://sairlab.org （AirSLAM）、SFU 3DLG https://3dlg-hcvc.github.io/ （Multi3DRefer）、Ai2 https://allenai.org （Molmo）、RAI Institute https://rai-inst.com/ （VLFM）、NVIDIA SIL https://research.nvidia.com/labs/sil/ （GEN3C）、Intel ISL https://github.com/isl-org （MiDaS、DPT）
     - 澳洲：Adelaide AIML https://adelaide.edu.au/research/australian-institute-for-machine-learning/ （NavGPT）、QUT QVPR https://github.com/QVPR （Patch-NetVLAD）
     - 從奠基論文的作者回推：清華 IVG https://ivg.au.tsinghua.edu.cn/ （UniGoal、StreamVGGT）、清華 THU-SI https://github.com/THU-SI （Spatial-MLLM）、清華 Li Yi https://ericyi.github.io/ （OmniSpatial）、北大 HMI Lab https://github.com/PKU-HMI-Lab （RoboRefer）、浙大 Wenguan Wang https://sites.google.com/view/wenguanwang （3DGS Survey）、上海科大 SVIP https://svip-lab.github.io/ （2D Gaussian Splatting）、Intellindust AI Lab https://github.com/Intellindust-AI-Lab （DEIM）、中研院資訊所 https://www.iis.sinica.edu.tw/en/ （YOLOv7）、Kyung Hee Networking Intelligence Lab http://networking.khu.ac.kr/ （MobileSAM）、Berkeley AUTOLAB https://autolab.berkeley.edu/ （LERF）、Berkeley BAIR https://bair.berkeley.edu/ （MonST3R）、Harvard VCG https://vcg.seas.harvard.edu （LangSplat）、MIT Scene Representation Group https://scenerepresentations.org/ （pixelSplat）、Yunzhu Li https://yunzhuli.github.io/ （PhysTwin）、Oregon State Stefan Lee https://web.engr.oregonstate.edu/~leestef/ （VLN-CE）、ENPC IMAGINE https://imagine-lab.enpc.fr/ （SuGaR）、TUM Visual Computing & AI https://niessnerlab.org/ （ScanRefer）、KAUST IVUL https://ivul.kaust.edu.sa/ （PointNeXt）
     - ETH CVG https://cvg.ethz.ch （3D 視覺、SLAM）、Princeton VL https://pvl.cs.princeton.edu （SLAM、深度）、Bonn PRBonn https://www.ipb.uni-bonn.de （LiDAR、SLAM）、CMU LeCAR https://lecar-lab.github.io/ （足式控制）
   - 查法：看上列頁面近期發表，或 WebSearch `<機構> <主題關鍵字> <年月>`。
1. **arXiv 新投稿**：
   - 主要用 RSS：`https://rss.arxiv.org/rss/cs.RO`、`https://rss.arxiv.org/rss/cs.CV`，一次請求拿到當天全部新投稿，再用下表關鍵字比對標題與摘要。RSS 只有當天，距上次更新超過一天的日子用下一項補。
   - 補查漏掉的日期用 arXiv API：`https://export.arxiv.org/api/query`（只能用 https，http 在雲端連不上），`search_query` 加 `submittedDate:[上次更新日 TO 今天]`，`sortBy=submittedDate`，`max_results=100`。請求間隔 3 秒以上，429 就退避重試；被擋住時在 PR 註明哪幾天沒查到。
   - **HF Daily Papers**：`https://huggingface.co/api/daily_papers?date=YYYY-MM-DD` 逐日查，挑與範圍相關的；按讚數是收錄條件「HF」的依據。
   - WebFetch 失敗時改用 curl。

   | 主題 | 分類 | 關鍵字（abs 或 ti，OR 串接） |
   |---|---|---|
   | vln | cs.RO, cs.CV | "vision-language navigation", "object goal navigation", "embodied navigation", "navigation foundation model" |
   | local-nav | cs.RO | "visual navigation" AND (diffusion OR "world model" OR "reinforcement learning"), "end-to-end navigation" |
   | semantic-map | cs.RO, cs.CV | "scene graph", "open-vocabulary map", "semantic mapping" |
   | quadruped | cs.RO | (quadruped OR legged) AND (perceptive OR navigation OR terrain) |
   | wheel-legged | cs.RO | "wheel-legged", "wheeled-legged", "legged-wheeled" |
   | slam | cs.RO, cs.CV | SLAM, "visual odometry", "LiDAR-inertial", "place recognition", relocalization |
   | reconstruction | cs.CV, cs.RO | "feed-forward reconstruction", "3D reconstruction" AND (VGGT OR pointmap), "structure from motion", "Gaussian splatting" |
   | perception-3d | cs.CV, cs.RO | "depth estimation", "stereo matching", occupancy |
   | det3d | cs.CV, cs.RO | "3D object detection" AND (indoor OR open-vocabulary), "3D instance segmentation", "point cloud" AND (segmentation OR backbone) |
   | spatial | cs.CV, cs.RO | "3D visual grounding", "spatial reasoning" AND (VLM OR "vision-language"), "3D LLM" |
   | vision | cs.CV | "open-vocabulary detection", "open-vocabulary segmentation", "vision foundation model", "real-time object detection", YOLO |
   | real2sim | cs.RO, cs.CV | "real-to-sim", real2sim, "digital twin" AND robot, "Gaussian splatting" AND simulation |

2. **補充來源**（WebSearch）：Science Robotics、T-RO、IJRR、RA-L、T-ASE、JFR、TPAMI、IJCV 新刊；當期 RSS / CoRL / ICRA / IROS / CVPR / ICCV / ECCV / 3DV / SIGGRAPH / WACV / NeurIPS / ICLR / ICML 接收論文；EMNLP、ACL 只看 VLN 相關。
   **會議接收名單**：名單一公布就逐一比對，不只靠 arXiv 關鍵字。2026-11 抽樣 RSS、ECCV 2026，人工判定範圍內 146 篇只收到 10 篇，其中 6 篇 venue 還停在 arXiv。可用來源：`roboticsconference.org/<年>/program/papers/`、`www.roboticsproceedings.org/rss<屆>/index.html`、`eccv.ecva.net/virtual/<年>/papers.html`。接收論文常沒有寫進 arXiv Comments，也可能換標題（LingBot-Map 官方名單上沒有 LingBot），所以比對時要連 `metrics.json` 的標題一起看。arXiv 標題搜尋 47/135 查不到，要再用 Semantic Scholar `paper/search/match` 補。

3. **篩選**：只有 arXiv、還沒正式刊登的論文，只收第 0 步主要名單（NVIDIA、企業、實驗室；不含擴充追蹤名單）內的企業與實驗室（官方 repo star ≥ 500 或使用者推薦的除外）；已被會議或期刊接收的不限機構。每主題每次最多收 5 篇，NVIDIA 的不佔名額。名額優先給第 0 步主要名單內的機構，其次依：有實機實驗 > 開源程式或權重 > 標準 benchmark 上宣稱 SOTA。純 benchmark 微幅改進、只在遙測或醫療影像上驗證的不收。機構以 arXiv 摘要頁或論文首頁的作者單位為準，「機構」欄要填。

## 得獎名單（擴充重要論文時查）

查 CVPR、ICCV、ECCV、3DV、ICRA、IROS、CoRL、RSS 的最佳論文（含入圍、honorable mention、各類別獎），符合範圍的收進 `classics.csv` 並標 `獲獎`。2021–2026 已全面查過一次（2026-10），之後每年各會議公布後補當年度。

| 會議 | 來源 | 坑 |
|---|---|---|
| CVPR | `cvpr.thecvf.com/Conferences/<年>/News/...`、候選 `cvpr.thecvf.com/virtual/<年>/events/AwardCandidates<年>` | 2022 finalists、2024 candidates 沒有官方清單；IEEE TCPAMI 獎項頁有年份與獎項標錯，別當來源 |
| ICCV / ECCV | `iccv<年>.thecvf.com`、`eccv<年>.ecva.net/virtual/<年>/awards_detail` | ICCV 候選名單多半不公開，只能從 ICCV Daily（rsipvision.com）零星找到 |
| 3DV | `3dvconf.github.io/<年>/awards/` 與同目錄 `award_candidates.csv` | 2021、2024 官網沒有得獎頁，只能靠大學新聞；2023 停辦 |
| ICRA | `<年>.ieee-icra.org/awards/`；2021 只有 RAS 獎項手冊 PDF；2022、2023 用 Robohub 轉載 | 官網常只列入圍，得獎者要等會後 |
| IROS | `<年>.ieee-iros.org/program/awards/`；2023 用 AIhub 轉載 | curl 直接抓官網會 403，改用 WebFetch；2021 網域已失效、2024 官網與 PaperCept 都擋；2025 只列入圍、不分獎項 |
| CoRL / RSS | `<年>.corl.org/program/awards`、`roboticsconference.org/<年>/program/awards/` | CoRL 2022 網域已轉走；RSS 2023、2024 官網只列入圍 |

- 得獎與否以官網為準；只有二手報導（新聞、X、實驗室網站）的寫成入圍，不寫得獎。
- 純操作、純人形、純自駕、無人機、純渲染品質改進的不收，即使得獎。

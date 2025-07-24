# Enterprise Data Architecture Toolkit

This GitHub repository contains a full set of tools to support Enterprise Data Architecture delivery across 6 key roadmap stages, based on the Pragmatic Architect methodology:  
🔗 https://pragmaticarchitect.wordpress.com/2011/03/05/how-to-build-a-roadmap/

---

## 📦 Toolkit Structure

- All tools are built in **Python + Streamlit**
- Runs **locally**, 100% offline
- Sample data preloaded (`sample_data/`)
- One folder per stage, with `.py` scripts for each tool

### 📁 Folder Breakdown

```
eda_full_toolkit/
├── tools/
│   ├── stage1_define_current_state/
│   ├── stage2_define_future_state/
│   ├── stage3_gap_analysis/
│   ├── stage4_prioritize_execute/
│   ├── stage5_mobilize/
│   └── stage6_monitor_govern/
├── sample_data/
└── README.md
```

---

## 🧰 What's Inside

| Stage | Tools |
|-------|-------|
| Stage 1 - Define Current State | System Inventory Tracker, Capability Heatmap, Business Process Mapper, Data Entity Catalogue, Technology Landscape |
| Stage 2 - Define Future State | Target Architecture Blueprint, Capability Matrix, Tech Fit-Gap Matrix |
| Stage 3 - Gap Analysis | Capability Gap Matrix, Data Quality Gap, Integration Gaps |
| Stage 4 - Prioritize & Execute | Initiative Prioritization, Execution Roadmap, Dependency Tracker, Risk Register, Resourcing Plan |
| Stage 5 - Mobilize | Workstream Tracker, Onboarding Plan, Comms Plan, KPI Baseline Tracker |
| Stage 6 - Monitor & Govern | Compliance Dashboard, KPI Monitor, Incident Log, Steward Log, Audit Reporting |

---

## 🚀 How to Use

Install dependencies:
```bash
pip install streamlit pandas
```

Run any tool (example):
```bash
cd tools/stage1_define_current_state
streamlit run system_inventory_tracker.py
```

Or browse all `.py` files under any `tools/stage*/` folder.

---

## 🙌 Built With

- Python 3
- Streamlit
- A few cups of chai and late-night consulting memories
- Inspiration from DAMA DMBOK, TOGAF, and CMMI frameworks
- Plus some vibecoding using Claude AI, ChatGPT, and GitHub Copilot

---

## 🔗 Author

Vishant Bhat — [https://github.com/vishantbhat](https://github.com/vishantbhat)  
This project is shared to help data engineers, architects, and transformation leaders accelerate their journeys 🚀
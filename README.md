# 🧭 Enterprise Data Architecture Tools

This toolkit is designed for enterprise architects and data leaders to define and communicate current and future state architecture using the 5-step roadmap approach inspired by the Pragmatic Architect framework.

All tools are:
- 🔒 Fully offline & self-hosted (Streamlit-based)
- 🖥️ Compatible with Linux Mint & LibreOffice
- 🎯 Built for fast demo in interviews or client consulting engagements

---

## 📦 Tools Overview

### 1. [System Inventory Tracker](tools/system_inventory_tracker)
> Catalog current systems, their purpose, tech stack, dependencies, and business alignment.
- Add and manage system metadata
- Export to CSV or YAML

### 2. [Capability Heatmap](tools/capability_heatmap)
> Visual matrix showing how well systems support key business capabilities.
- Color-coded support levels (Full / Partial / None)
- Add capabilities and systems interactively
- Export heatmap to CSV

### 3. [Technology Landscape Matrix](tools/technology_landscape_matrix)
> Document technology stack across lifecycle stages and usage patterns.
- Tag tools as Strategic / Tolerated / Sunset
- Classify usage type (Core, Peripheral, etc.)
- Export matrix to CSV

### 4. [Data Flow Mapper](tools/data_flow_mapper)
> Define and visualize integrations between systems.
- Specify source/target systems, interfaces, protocols
- Auto-generate flow diagram using Graphviz
- Export flow table as CSV

### 5. [Technical Debt Register](tools/technical_debt_register)
> Track and prioritize architecture or implementation debt.
- Log issues, root causes, proposed fixes, risk level
- Status tracking (Identified → Resolved)
- Export register to CSV

---

## ▶️ Running the Tools

Each tool runs independently. To launch:

```bash
cd tools/<tool_name>
pip install -r requirements.txt
streamlit run app.py

import streamlit as st

st.set_page_config(page_title="EDA Toolkit Launcher", layout="wide")
st.title("🚀 EDA Toolkit Launcher")

st.markdown("## 📍 Roadmap Stage: Define Current State")

tools = {
    "System Inventory Tracker": "tools/system_inventory_tracker/app.py",
    "Capability Heatmap": "tools/capability_heatmap/app.py",
    "Technology Landscape Matrix": "tools/technology_landscape_matrix/app.py",
    "Data Flow Mapper": "tools/data_flow_mapper/app.py",
    "Technical Debt Register": "tools/technical_debt_register/app.py"
}

for name, path in tools.items():
    st.write(f"🔹 **{name}**")
    st.code(f"streamlit run {path}", language="bash")

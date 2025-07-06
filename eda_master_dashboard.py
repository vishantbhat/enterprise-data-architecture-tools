import streamlit as st
import subprocess

st.set_page_config(page_title="EDA Toolkit Launcher", layout="wide")
st.title("🚀 EDA Toolkit Launcher")

tools = {
    "System Inventory Tracker": "tools/system_inventory_tracker/app.py",
    "Capability Heatmap": "tools/capability_heatmap/app.py",
    "Technology Landscape Matrix": "tools/technology_landscape_matrix/app.py",
    "Data Flow Mapper": "tools/data_flow_mapper/app.py",
    "Technical Debt Register": "tools/technical_debt_register/app.py"
}

for name, path in tools.items():
    if st.button(f"▶️ Launch {name}"):
        st.write(f"Launching {name}...")
        subprocess.Popen(["streamlit", "run", path])

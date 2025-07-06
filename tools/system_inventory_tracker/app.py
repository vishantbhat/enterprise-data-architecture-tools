import streamlit as st
import pandas as pd
import yaml
from io import BytesIO

# Page Config
st.set_page_config(page_title="System Inventory Tracker", layout="wide")
st.title("📊 System Inventory Tracker")

# Initialize session state
if "inventory" not in st.session_state:
    st.session_state.inventory = []

# Sidebar: Add New System
st.sidebar.header("➕ Add New System")
with st.sidebar.form("add_system_form"):
    system_name = st.text_input("System Name")
    owner = st.text_input("System Owner")
    function = st.text_area("Primary Function")
    dependencies = st.text_area("Dependencies (comma-separated)")
    tech_stack = st.text_input("Technology Stack")
    business_process = st.text_input("Business Process Supported")
    risk_level = st.selectbox("Risk Level", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add System")

    if submitted and system_name:
        st.session_state.inventory.append({
            "System Name": system_name,
            "Owner": owner,
            "Function": function,
            "Dependencies": [d.strip() for d in dependencies.split(",") if d.strip()],
            "Technology Stack": tech_stack,
            "Business Process": business_process,
            "Risk Level": risk_level
        })
        st.success(f"System '{system_name}' added!")

# Display Inventory
st.subheader("📋 Current Inventory")
if st.session_state.inventory:
    df = pd.DataFrame(st.session_state.inventory)
    st.dataframe(df, use_container_width=True)

    # Export options
    col1, col2 = st.columns(2)
    with col1:
        csv_data = df.to_csv(index=False).encode('utf-8')

        if st.download_button("📥 Export as CSV", data=csv_data, file_name="system_inventory.csv", mime="text/csv"):
            st.success("CSV exported!")

    with col2:
        yaml_data = yaml.dump(st.session_state.inventory, sort_keys=False)
        if st.download_button("📥 Export as YAML", data=yaml_data, file_name="system_inventory.yaml"):
            st.success("YAML exported!")
else:
    st.info("No systems added yet.")

import streamlit as st
import subprocess

st.set_page_config(page_title="EDA Toolkit Launcher", layout="centered")
st.title("Enterprise Data Architecture Toolkit")

st.markdown("## Stage 1: Define Current State")
if st.button("System Inventory Tracker"):
    subprocess.Popen(["streamlit", "run", "tools/system_inventory_tracker/app.py"])
if st.button("Capability Heatmap"):
    subprocess.Popen(["streamlit", "run", "tools/capability_heatmap/app.py"])
if st.button("Technology Landscape Matrix"):
    subprocess.Popen(["streamlit", "run", "tools/technology_landscape_matrix/app.py"])
if st.button("Data Flow Mapper"):
    subprocess.Popen(["streamlit", "run", "tools/data_flow_mapper/app.py"])
if st.button("Technical Debt Register"):
    subprocess.Popen(["streamlit", "run", "tools/technical_debt_register/app.py"])

st.markdown("## Stage 2: Define Future State")
if st.button("Target State Architecture Blueprint"):
    subprocess.Popen(["streamlit", "run", "tools/target_state_architecture/app.py"])
if st.button("Capability Maturity Model"):
    subprocess.Popen(["streamlit", "run", "tools/capability_maturity_model/app.py"])
if st.button("Technology Fit-Gap Matrix"):
    subprocess.Popen(["streamlit", "run", "tools/technology_fit_gap/app.py"])
if st.button("High-Level Migration Plan"):
    subprocess.Popen(["streamlit", "run", "tools/high_level_migration_plan/app.py"])
if st.button("Transformation Principles Register"):
    subprocess.Popen(["streamlit", "run", "tools/transformation_principles/app.py"])
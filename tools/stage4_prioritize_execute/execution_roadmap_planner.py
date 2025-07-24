
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Execution Roadmap Planner", layout="wide")
st.title("Execution Roadmap Planner")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "execution_roadmap_planner.csv"))
if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df)
else:
    st.warning("Sample data not found.")

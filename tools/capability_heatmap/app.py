import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Capability Heatmap", layout="wide")
st.title("🗺️ Capability Heatmap")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "capability_matrix.csv"))
if os.path.exists(file):
    data = pd.read_csv(file)
    st.success("✅ Sample data loaded")
    st.dataframe(data, use_container_width=True)
    st.download_button("📥 Download as CSV", data=data.to_csv(index=False).encode("utf-8"), file_name="capability_matrix.csv", mime="text/csv")
else:
    st.warning("⚠️ Sample data file not found.")

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Technical Debt Register", layout="wide")
st.title("💣 Technical Debt Register")

file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sample_data", "technical_debt.csv"))
if os.path.exists(file):
    data = pd.read_csv(file)
    st.success("✅ Sample data loaded")
    st.dataframe(data, use_container_width=True)
    st.download_button("📥 Download as CSV", data=data.to_csv(index=False).encode("utf-8"), file_name="technical_debt.csv", mime="text/csv")
else:
    st.warning("⚠️ Sample data file not found.")

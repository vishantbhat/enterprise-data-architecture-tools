import streamlit as st
import pandas as pd

st.set_page_config(page_title="Capability Heatmap", layout="wide")
st.title("🗺️ Capability Heatmap")

# Initialize state
if "capabilities" not in st.session_state:
    st.session_state.capabilities = []
if "systems" not in st.session_state:
    st.session_state.systems = []
if "matrix" not in st.session_state:
    st.session_state.matrix = {}

# Sidebar: Add Capability
st.sidebar.header("➕ Add Capability / System")
with st.sidebar.form("add_form"):
    cap = st.text_input("Add Capability")
    sys = st.text_input("Add System")
    submit = st.form_submit_button("Add")
    if submit:
        if cap and cap not in st.session_state.capabilities:
            st.session_state.capabilities.append(cap)
        if sys and sys not in st.session_state.systems:
            st.session_state.systems.append(sys)

# Build matrix UI
st.subheader("📊 Capability-to-System Support Matrix")
support_levels = ["None", "Partial", "Full"]
support_colors = {"None": "red", "Partial": "orange", "Full": "green"}

matrix_data = []
for cap in st.session_state.capabilities:
    row = {"Capability": cap}
    for sys in st.session_state.systems:
        key = f"{cap}::{sys}"
        default = st.session_state.matrix.get(key, "None")
        row[sys] = st.selectbox(f"{cap} ↔ {sys}", options=support_levels, index=support_levels.index(default), key=key)
        st.session_state.matrix[key] = row[sys]
    matrix_data.append(row)

if matrix_data:
    df = pd.DataFrame(matrix_data)
    st.dataframe(df.style.applymap(lambda val: f"background-color: {support_colors.get(val, '')}", subset=st.session_state.systems), use_container_width=True)

    # Export to CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Heatmap as CSV", data=csv, file_name="capability_heatmap.csv", mime="text/csv")
else:
    st.info("Add capabilities and systems using the sidebar.")

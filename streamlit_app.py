import streamlit as st
import pandas as pd
from pathlib import Path

# Title block
st.title("Boeing Project Dashboard")

# 1. Point to your Excel Data 
EXCEL_PATH = Path(__file__).parent / "2027 Bean Counts.xlsx"

@st.cache_data
def load_data():
    try:
        return pd.read_excel(EXCEL_PATH, sheet_name=0)
    except Exception as e:
        # Fallback tracking display if the file paths encounter an error
        return pd.DataFrame({"Category": ["Error Loading Excel"], "Data": [str(e)]})

df = load_data()

# 2. Setup Sidebar Filter layout
st.sidebar.header("Filters")
if "Category" in df.columns:
    # Build unique option categories drop down menu
    categories = list(df["Category"].dropna().unique())
    selected_cat = st.sidebar.selectbox("Select Category:", categories)
    filtered_df = df[df["Category"] == selected_cat]
else:
    st.sidebar.write("No 'Category' column found.")
    filtered_df = df

# 3. Dynamic layout boxes
col1, col2 = st.columns([1, 3])

with col1:
    st.metric(label="Total Records", value=len(filtered_df))

with col2:
    st.subheader("Filtered Data View")
    st.dataframe(filtered_df, use_container_width=True)

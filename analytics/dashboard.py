import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Personal Finance Analytics",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Personal Finance Analytics")

st.write("Analytics dashboard for the Personal Finance Tracker")

st.header("Financial Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Income", "₱25,000")

with col2:
    st.metric("Total Expenses", "₱12,500")

with col3:
    st.metric("Balance", "₱12,500")

st.header("Sample Transactions")

data = {
    "Category": ["Food", "Transportation", "Bills", "Shopping"],
    "Amount": [3500, 1800, 4200, 3000]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.bar_chart(df.set_index("Category"))
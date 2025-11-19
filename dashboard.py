# dashboard.py — FIXED FOR MIXED TYPES ERROR
import streamlit as st
import polars as pl

st.title("Bloomberg Commodities – Fixed & Simple")

try:
    # df = pl.read_csv("data/combined_commodities.csv")
    df = pl.read_csv("data/combined_commodities_clean.csv")
    st.success(f"Loaded {len(df)} rows")

    # Select metric to plot (only numeric fields)
    numeric_cols = [col for col in df.columns if col not in ["Date", "Asset"] and df[col].dtype == pl.Float64]
    metric = st.selectbox("Select Field", numeric_cols)

    # Pivot, convert to Pandas, fill nulls
    chart_df = df.pivot(index="Date", columns="Asset", values=metric)
    chart_pd = chart_df.to_pandas().set_index("Date").fillna(0)  # Fill nulls + index on Date

    st.line_chart(chart_pd)
except Exception as e:
    st.error(f"Run pipeline.py first! Error: {e}")

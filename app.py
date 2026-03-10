import streamlit as st
import pandas as pd
import plotly.express as px
import json

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="West Java Poverty Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 West Java Poverty Analysis Dashboard")
st.caption("Analysis of poverty levels across districts in West Java (2019–2023)")

st.divider()

# =====================================
# LOAD DATA
# =====================================
@st.cache_data
def load_data():
    return pd.read_csv("kemiskinan_clean.csv")

@st.cache_data
def load_geo():
    with open("jabar_kabupaten.geojson") as f:
        return json.load(f)

df = load_data()
geojson = load_geo()

# =====================================
# DATA CLEANING
# =====================================
df["kabupaten_map"] = (
    df["kabupaten"]
    .str.replace("Kabupaten ", "", regex=False)
    .str.replace("Kab ", "", regex=False)
    .str.replace("Kota ", "", regex=False)
    .str.upper()
)

# =====================================
# SIDEBAR
# =====================================
st.sidebar.title("Dashboard Filter")

year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["tahun"].unique())
)

kabupaten = st.sidebar.selectbox(
    "Select District",
    sorted(df["kabupaten"].unique())
)

df_year = df[df["tahun"] == year]
df_kab = df[df["kabupaten"] == kabupaten]

# =====================================
# KPI SECTION
# =====================================
avg_poverty = df_year["persentase_miskin"].mean()
max_poverty = df_year.loc[df_year["persentase_miskin"].idxmax()]
min_poverty = df_year.loc[df_year["persentase_miskin"].idxmin()]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Poverty Rate",
    f"{avg_poverty:.2f}%"
)

col2.metric(
    "Highest Poverty",
    f"{max_poverty['kabupaten']}",
    f"{max_poverty['persentase_miskin']}%"
)

col3.metric(
    "Lowest Poverty",
    f"{min_poverty['kabupaten']}",
    f"{min_poverty['persentase_miskin']}%"
)

col4.metric(
    "Total Districts",
    df_year["kabupaten"].nunique()
)

st.divider()

# =====================================
# TREND CHART
# =====================================
col1, col2 = st.columns(2)

with col1:

    st.subheader("West Java Poverty Trend")

    trend = df.groupby("tahun")["persentase_miskin"].mean().reset_index()

    fig = px.line(
        trend,
        x="tahun",
        y="persentase_miskin",
        markers=True,
        color_discrete_sequence=["red"]
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.subheader(f"Poverty Trend: {kabupaten}")

    fig2 = px.line(
        df_kab,
        x="tahun",
        y="persentase_miskin",
        markers=True,
        color_discrete_sequence=["orange"]
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# =====================================
# BAR CHART TOP 10
# =====================================
st.subheader("Top 10 Districts with Highest Poverty Rate")

top10 = df_year.sort_values(
    "persentase_miskin",
    ascending=False
).head(10)

fig3 = px.bar(
    top10,
    x="persentase_miskin",
    y="kabupaten",
    orientation="h",
    color="persentase_miskin",
    color_continuous_scale="Reds"
)

fig3.update_layout(yaxis=dict(autorange="reversed"))

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# =====================================
# MAP
# =====================================
st.subheader("West Java Poverty Map")

fig_map = px.choropleth(
    df_year,
    geojson=geojson,
    locations="kabupaten_map",
    featureidkey="properties.KABKOT",
    color="persentase_miskin",
    color_continuous_scale="Reds",
    hover_name="kabupaten",
    hover_data=["persentase_miskin"]
)

fig_map.update_geos(
    fitbounds="locations",
    visible=False
)

fig_map.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0}
)

st.plotly_chart(fig_map, use_container_width=True)

st.divider()

# =====================================
# RANKING TABLE
# =====================================
st.subheader("District Poverty Ranking")

ranking = df_year.sort_values(
    "persentase_miskin",
    ascending=False
)

st.dataframe(ranking, use_container_width=True)

st.divider()

# =====================================
# INSIGHT
# =====================================
st.subheader("Key Insight")

st.info(
    f"""
In {year}, the district with the highest poverty rate is **{max_poverty['kabupaten']}**
with **{max_poverty['persentase_miskin']}%**, while the lowest poverty rate occurs in
**{min_poverty['kabupaten']}** with **{min_poverty['persentase_miskin']}%**.
"""
)
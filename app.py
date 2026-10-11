
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Visualization Dashboard")

data = {
    "Country": ["India", "USA", "Japan", "UK", "China"],
    "Population": [140, 33, 12, 7, 141],
    "GDP": [3.7, 27, 4.2, 3.3, 17]
}

df = pd.DataFrame(data)

st.subheader("Dataset")
st.write(df)

st.subheader("Population Comparison")
fig = px.bar(
    df,
    x="Country",
    y="Population",
    title="Population by Country"
)
st.plotly_chart(fig)

st.subheader("GDP Comparison")
fig2 = px.scatter(
    df,
    x="Country",
    y="GDP",
    title="GDP by Country"
)
st.plotly_chart(fig2)

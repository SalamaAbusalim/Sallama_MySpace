import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

df = pd.read_csv("data.csv", sep=";")
col1, col2,col3 = st.columns([3,0.2,3])
with col1:
    for index, row in df.iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.write(f"[Ream more]({row['url']})")

with col3:
    st.image("2.jpg")

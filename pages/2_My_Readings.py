import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")


df_ar = pd.read_csv("Ar_data.csv", sep=";")
df_en = pd.read_csv("En_data.csv", sep=";")
col1, col2,col3 = st.columns([3,0.5,3])
with col3:
    for index, row in df_ar.iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.write(f"[أقرأ المزيد]({row['url']})")

st.markdown('---')
with col1:
    st.header('')
    st.image('img2.jpg')
col4, col5,col6 = st.columns([3,0.5,3])
with col4:
    for index, row in df_en.iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.write(f"[Ream more]({row['url']})")
with col6:
    st.image('2.jpg')



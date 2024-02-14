import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")
col1, col2,col3 = st.columns([4,.3,5])
with col3:
    st.title("..كيف نجوت؟ حتى الآن")
    with open('writings.txt', 'r', encoding='utf8') as file:
        content = file.read()
    st.write(content)

with col1:
    st.header('')
    st.header('')
    st.header('')
    st.header('')
    st.image('3.jpg')
    st.header('')


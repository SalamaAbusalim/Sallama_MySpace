import streamlit as st
st.set_page_config(layout="wide")
with st.columns(3)[2]:
    st.title("المحراب")

col1, col2 = st.columns(2)

with col1:
    st.image("IMG_2691.jpg")
with col2:
    st.write("اسمي سلّامة (بتشديد اللام). في هذه المساحة أشارك بعض ما أحب في الحياة")
    st.write(" ")
    st.text_input("لماذا هذه الصورة؟")
    button1 = st.button(label="حكمة اليوم")
    if button1:
        st.write("أحب الأعمال الى الله ادومها وان قل")

import streamlit as st
st.set_page_config(layout="wide")

col2, col2, col3 = st.columns([3,1.7,3])
col4, col5, col6 = st.columns([1,4,1])
with col2:
    button = st.button("Open the Quote", type= "primary")
if button:
    with col5:
        st.header("")
        st.header("سددوا وقاربوا وأبشروا.. واعلموا أن أحب الأعمال الى الله أدومها وإن قل")
        st.header(" ")
        st.header("فاذكروني أذكركم.. واشكروا لي ولا تكفرون")



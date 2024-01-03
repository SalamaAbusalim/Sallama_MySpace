import streamlit as st
from send_email import send_email

st.header("Contact me")


user_email = st.text_input("Your email")
raw_message = st.text_area("Your message")
button = st.button("Send")
message = f"""\
Subject: You received a new message

From:{user_email}
{raw_message}
"""

if button:
    send_email(message)
    st.info("Your message was sent successfully")


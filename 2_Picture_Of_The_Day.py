import streamlit as st
import requests

api_key="iD3P8fabJ35SCVLC9Ue4cOwCFnpIt5CxvzVsLGUi"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()
title = content["title"]
image_link = content["hdurl"]
description = content["explanation"]
st.title(title)
st.image(image_link)
st.write(description)

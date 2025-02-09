import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import validators


from app.nav import SideBarLinks
from app.title_scrape import get_title
SideBarLinks()

st.session_state['url_validated'] = False

st.title("See Your Degree Track!")

url = st.text_input("Enter the URL to your degree's requirements").strip()
degree = ""

if url:
    if not validators.url(url):
        st.error("We couldn't reach that URL... Try again?")
    else:
        degree = get_title(url)
        if degree == "Page Not Found":
            st.error("We couldn't reach that URL... Try again?")

    if degree:
        st.subheader(f"**Is this your degree?** ***{degree}***")

        if st.button("Yes!"):
            st.session_state['url_validated'] = True
            st.session_state['degree'] = degree,
            st.session_state['url'] = url,
            st.switch_page("pages/display_classes.py")
       
            
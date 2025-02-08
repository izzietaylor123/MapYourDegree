import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def get_title(url):
    # Send HTTP request
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the full title
    title = soup.title.string

    # Split the title to get the first part ("Computer Science")
    title_parts = title.split("<")
    main_title = title_parts[0].strip()  # Remove any leading/trailing spaces

    # Print the extracted title
    print(main_title)

    # Print the extracted title
    return (main_title)

st.title("See Your Degree Track!")
st.write("Please input your major url to continue.")

url = st.text_input("Degree URL")
if url:

    degree = get_title(url)

    st.write(f"**Is this your degree?** {degree}")

    if st.button("Yes!"):
        st.session_state['degree'] = degree,
        st.session_state['url'] = url,
        st.switch_page("pages.display_classes.py")
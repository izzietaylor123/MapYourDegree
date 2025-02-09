
import streamlit as st


def Search():
    st.sidebar.page_link("pages/enter_degree.py", label="Back to Degree Search", icon="🔎")


def AboutPageNav():
    st.sidebar.page_link("pages/about.py", label="About Map Your Degree", icon="🗺️")

def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def SideBarLinks():

    st.sidebar.image("logo.jpeg", width=150)


    HomeNav()

    if 'url_validated' not in st.session_state:
        st.session_state['url_validated'] = False

  
    if st.session_state['url_validated'] == True:
        Search()

    
    AboutPageNav()



# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def Search():
    st.sidebar.page_link("pages/enter_degree.py", label="Back to Degree Search", icon="🔎")


def AboutPageNav():
    st.sidebar.page_link("pages/about.py", label="About Map Your Degree", icon="🧠")

def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def SideBarLinks():
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("logo.jpeg", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page

    HomeNav()

    if st.session_state['url_validated'] == True:
        # Show the Home page link (the landing page)
        Search()

    # Show the other page navigators depending on the users' role.
    
    # Always show the About page at the bottom of the list of links
    AboutPageNav()



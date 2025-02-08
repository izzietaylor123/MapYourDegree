# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")



def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About NU.Compass", icon="🧠")


#### ------------------------ Examples for Role of mentee_student ------------------------

def menteeHomeNav():
    st.sidebar.page_link(
        "pages/00_Mentee_Home.py", label="Mentee Student Home", icon="👤")
    if st.session_state['program'] != -1:
        st.sidebar.page_link("pages/05_Programs.py", label="Back to Search", icon="🔍")



## ------------------------ Examples for Role of mentor_student ------------------------
def mentor_student_home():
    st.sidebar.page_link("pages/10_Mentor.py", label="Mentor Student Home", icon="👤")
    if st.session_state['program'] != -1:
        st.sidebar.page_link("pages/05_Programs.py", label="Back to Search", icon="🔍")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )


#### ------------------------ Global Experience Staff Member ------------------------
def AdminPageNav():

    st.sidebar.page_link("pages/20_IT_Admin_Home.py", label="System Admin", icon="🖥️")

def GEOPageNav():
    st.sidebar.page_link("pages/26_GEOAdmin_Home.py", label="GEO Admin", icon='🔍')
# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/compass.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # If the user role is a mentee_student
        if st.session_state["role"] == "mentee_student":
            menteeHomeNav()

        # If the user role is mentor student 
        if st.session_state["role"] == "mentor_student":
            mentor_student_home()


        # If the user is an IT administrator
        if st.session_state["role"] == "administrator":
            AdminPageNav()

        # If the user is a Global Experience Staff Member
        if st.session_state["role"] == "GESM":
            GEOPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")

import streamlit as st

from app.nav import SideBarLinks
st.session_state['url_validated'] = False

SideBarLinks()

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Import Lobster font */
    @import url('https://fonts.googleapis.com/css2?family=Lobster:wght@300&display=swap');

    /* Full-page centering */
    .stApp {
        background-color: #800020 !important; /* Burgundy */
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }

    /* Title styling */
    .title-text {
        color: #FFFDD0 !important; /* Cream */
        font-size: 10vh;
        font-weight: 300;
        text-align: center;
        font-family: 'Lobster', cursive !important;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-text">Map Your Degree</h1>', unsafe_allow_html=True)

# Button inside the scroll (Streamlit button functionality)
if st.button("Plan Your Degree", key="plan_degree", use_container_width=True):
    st.switch_page("pages/enter_degree.py")

# Video path (adjust if necessary)
video_path = "ca.mp4"  # Ensure the path is correct

# Streamlit video player with autoplay and muted, no loop here directly
st.video(video_path, start_time=0)
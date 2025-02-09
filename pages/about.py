import streamlit as st
from app.nav import SideBarLinks

SideBarLinks()

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
    .about-title {
        color: #FFFDD0 !important; /* Cream */
        font-size: 10vh;
        font-weight: 300;
        text-align: center;
        font-family: 'Lobster', cursive !important;
        margin-bottom: 2rem;
    }

    /* Scroll container (Fully Centered) */
    .scroll-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        flex-direction: column; /* Stacks button and scroll vertically */
    }

    .scroll-container {
        background: #F5F5DC; /* Beige parchment color */
        width: 35vw;
        max-width: 500px;
        min-height: 65vh;
        padding: 3rem 2rem;
        text-align: center;
        border-radius: 20px;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3), 0 5px 15px rgba(0, 0, 0, 0.5);
        border-left: 12px solid #d2b48c;
        border-right: 12px solid #d2b48c;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }

    /* Scroll text */
    .scroll-text {
        color: #800020;
        font-size: 4vh;
        font-family: 'Lobster', cursive;
        text-align: center;
        max-width: 80%;
        margin-bottom: 1.5rem; /* Moves button up */
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<h1 class="about-title">About Map Your Degree</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="scroll-wrapper">
        <div class="scroll-container">
            <p class="scroll-text">
                Map Your Degree was created with one purpose in mind: to help aspiring students of all majors plan their 
        roadmaps to obtaining a college degree. We wanted to create an interactive website that provides 
        Northeastern students with the necessary data and visuals to make informed and smart decisions about
        their academic careers, ultimately giving much needed clarity to the complicated Degree Audit System.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
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

    .styled-button {
        background-color: #800020;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 14px 28px; /* Increased padding for a better look */
        border-radius: 12px; /* Rounded corners */
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        position: absolute;
        bottom: 30px; /* Button positioned inside scroll */
        left: 50%;
        transform: translateX(-50%);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }


    .styled-button:hover {
        background-color: #800000;
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* More pronounced shadow on hover */
    }

    .styled-button:active {
        background-color: #660000;
        transform: scale(1.02); /* Slightly smaller when clicked */
    }

    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-text">Map Your Degree</h1>', unsafe_allow_html=True)

# Scroll container with button inside it
st.markdown("""
    <div class="scroll-wrapper">
        <div class="scroll-container">
            <p class="scroll-text">
                This is your official degree scroll! 🎓📜
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Button inside the scroll (Streamlit button functionality)
if st.button("Plan Your Degree", key="plan_degree", use_container_width=True):
    st.switch_page("pages/enter_degree.py")

import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Map Your Degree", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Import Lobster font */
        @import url('https://fonts.googleapis.com/css2?family=Lobster:wght@300&display=swap');

        .stApp {
            background-color: #800020 !important; /* Burgundy */
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .title-text {
            color: #FFFDD0 !important; /* Cream */
            font-size: 15vw; /* Dynamic scaling based on screen width */
            font-weight: 300; /* Less bold */
            text-align: center;
            font-family: 'Lobster', cursive !important; /* Ensure font is applied */
            line-height: 1.2; /* Adjust spacing */
        }
        header {
            background-color: #F5F5DC !important; /* Beige */
        }
        #MainMenu, footer, header .css-18e3th9 {
            visibility: hidden;
            height: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Display title with cursive font
st.markdown('<h1 class="title-text">Map Your Degree</h1>', unsafe_allow_html=True)

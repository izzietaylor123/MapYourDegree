import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Map Your Degree", layout="wide")

# Use custom CSS to apply a burgundy background, center extra-large text, and make the top bar beige
st.markdown("""
    <style>
        /* Override Streamlit default background */
        .stApp {
            background-color: #800020 !important; /* Burgundy */
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        /* Center and style the heading */
        .title-text {
            color: #FFFDD0; /* Cream */
            font-size: 100rem; /* EVEN BIGGER font */
            font-weight: bold;
            text-align: center;
        }
        /* Change top toolbar (Streamlit header) to beige */
        header {
            background-color: #F5F5DC !important; /* Beige */
        }
        /* Hide the menu & footer toolbar */
        #MainMenu, footer, header .css-18e3th9 {
            visibility: hidden;
            height: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Display the text in the center
st.markdown("<h1 class='title-text'>Map Your Degree</h1>", unsafe_allow_html=True)


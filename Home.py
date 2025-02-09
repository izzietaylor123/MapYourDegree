import streamlit as st

st.markdown(
    """
    <style>
    .image-container {
        position: absolute;
        top: 10px;
        left: 10px;
        z-index: 100;
    }

    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #000000;
        font-family: 'Merriweather', serif;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }
    
    .styled-button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .styled-button:hover {
        background-color: #800000;
    }
    </style>
    """, unsafe_allow_html=True)

image_path = "./logo.jpeg"

col1, col2 = st.columns([0.5, 4])  # Adjust column width to control image positioning

with col1:
    st.image(image_path, width=100)

with col2:
    st.markdown('<div class="title">Map Your Degree</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("Plan Your Degree", key="plan_degree", use_container_width=True):
        st.switch_page("pages/enter_degree.py")
    st.markdown('</div>', unsafe_allow_html=True)
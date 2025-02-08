import streamlit as st

st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #800000;
        font-family: 'Indie Flower', cursive;
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
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title">Map Your Degree</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("Plan Your Degree", key="plan_degree", use_container_width=True):
        st.switch_page("pages/enter_degree.py")
    st.markdown('</div>', unsafe_allow_html=True)
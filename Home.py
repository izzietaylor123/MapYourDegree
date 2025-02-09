import streamlit as st

st.markdown(
    """
    <style>
    /* Import Lobster font */
        @import url('https://fonts.googleapis.com/css2?family=Lobster:wght@300&display=swap');

        .stApp {
            background-color: #800020 !important; /* Burgundy */
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        /* Title at the top (Cursive restored) */
        .title-text {
            color: #FFFDD0 !important; /* Cream */
            font-size: 10vh; /* Large but readable */
            font-weight: 300; /* Less bold */
            text-align: center;
            font-family: 'Lobster', cursive !important;
            margin-bottom: 3rem; /* Space between title and scroll */
        }

        /* Main parchment scroll */
        .scroll-container {
            background: #F5F5DC; /* Beige parchment color */
            width: 35vw; /* Thinner for realism */
            max-width: 500px;
            min-height: 70vh; /* Taller for a scroll look */
            padding: 4rem 2rem;
            text-align: center;
            border-radius: 20px; /* Soft corners */
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3), 0 5px 15px rgba(0, 0, 0, 0.5);
            border-left: 12px solid #d2b48c; /* Side roll effect */
            border-right: 12px solid #d2b48c;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }

        /* Rolled edges (Swirl effect like 📜 emoji) */
        .scroll-container::before,
        .scroll-container::after {
            content: "";
            position: absolute;
            left: 50%;
            width: 200%; /* Extend for a wide scroll effect */
            height: 60px;
            background: linear-gradient(to bottom, #d2b48c, #F5F5DC); /* Gradient for depth */
            border-radius: 50%;
            transform: translateX(-50%);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3);
        }

        .scroll-container::before {
            top: -45px; /* Top swirl */
        }

        .scroll-container::after {
            bottom: -45px; /* Bottom swirl */
        }

        /* Scroll text inside */
        .scroll-text {
            color: #800020; /* Burgundy */
            font-size: 4vh;
            font-family: 'Lobster', cursive;
            text-align: center;
            max-width: 80%;
        }

        /* Hide Streamlit default UI elements */
        header {
            background-color: #F5F5DC !important;
        }
        #MainMenu, footer, header .css-18e3th9 {
            visibility: hidden;
            height: 0;
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

st.markdown('<h1 class="title-text">Map Your Degree</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="scroll-container">
        <p class="scroll-text">
            This is your official degree scroll! 🎓📜
        </p>
    </div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("Plan Your Degree", key="plan_degree", use_container_width=True):
        st.switch_page("pages/enter_degree.py")
    st.markdown('</div>', unsafe_allow_html=True)
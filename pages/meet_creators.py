import streamlit as st
import streamlit.components.v1 as components
from app.nav import SideBarLinks

SideBarLinks()

st.title("Meet the Team")

# Replace with your actual LinkedIn public usernames
linkedin_profiles = {
    "Person 1": "isabeltaylor412",
    "Person 2": "shelby-snyder-277a94268",
    "Person 3": "zaraceraj",
    "Person 4": "sukira-harris-9aba9b2a1"
}

# Function to generate LinkedIn embed code
def linkedin_embed(username):
    return f"""
        <script src="https://platform.linkedin.com/badges/js/profile.js" async defer></script>
        <div class="LI-profile-badge" data-version="v1" data-size="large" data-locale="en_US"
             data-type="horizontal" data-theme="light" data-vanity="{username}">
        </div>
    """

# Create a 2x2 layout using Streamlit columns
col1, col2 = st.columns(2)

# First row
with col1:
    st.subheader("Isabel Taylor")
    components.html(linkedin_embed(linkedin_profiles["Person 1"]), height=400)

with col2:
    st.subheader("Shelby Snyder")
    components.html(linkedin_embed(linkedin_profiles["Person 2"]), height=400)

# Second row
col3, col4 = st.columns(2)

with col3:
    st.subheader("Zara Ceraj")
    components.html(linkedin_embed(linkedin_profiles["Person 3"]), height=400)

with col4:
    st.subheader("Sukira Harris")
    components.html(linkedin_embed(linkedin_profiles["Person 4"]), height=400)

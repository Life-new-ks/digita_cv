import streamlit as st
from config import PAGE_TITLE, PAGE_ICON
from pages import home, about, projects

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

page = st.sidebar.radio("Navigate", ["Home", "About", "Projects"])

if page == 'Home':
    home.show()

elif page == 'About':
    about.show()

elif page == 'Projects':
    projects.show()

import streamlit as st

pages = {
    "Main": [
        st.Page("1_home.py", title="Home", icon="🏠"),
        st.Page("2_about.py", title="About", icon="👤"),
        st.Page("3_projects.py", title="Projects", icon="💻"),
        st.Page("4_lessons.py", title="Lessons", icon="👨‍🏫"),

    ],
    'Lessons':[
        st.Page('lessons/lesson_12.py', title='Lesson 12: SQL Intro', icon='📖', visibility="hidden")
    ]
}

navigation = st.navigation(pages)

navigation.run()


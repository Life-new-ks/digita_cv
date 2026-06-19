import streamlit as st

st.title("Lesson 12")

st.write(
    """
## Lesson summary

In this lesson, we learned:

- How Streamlit pages work
- How to use `st.Page`
- How to use `st.navigation`
- How to move between pages
"""
)

st.page_link(
    "4_lessons.py",
    label="Back to Lessons",
    icon="⬅️",
)

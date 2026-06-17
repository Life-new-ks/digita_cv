import streamlit as st
from config import EMAIL, LINKEDIN_URL

def show():

    st.title("About Me")
    st.write("""
    Hi there! I'm Camazing CATie, a passionate and dedicated cat with a love for napping and purring. I have a knack for finding the purr-fect solution to any problem, whether it's finding the coziest spot in the house or catching that elusive toy. With my strong communication skills and agility, I'm always ready to provide companionship and support to those around me. When I'm not busy patrolling the premises or lounging in the sun, you can find me exploring new adventures and making new friends. Feel free to connect with me on LinkedIn or drop me an email – I'm always up for a chat about cats, napping techniques, or anything else that piques my interest!
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")

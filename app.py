import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jeta Kryeziu"
PAGE_ICON = ":wave:"
NAME = "Jeta Kryeziu"
DESCRIPTION = """
Data Scientist specializing in spatial-sensor data and data-driven decision-making.
"""

EMAIL = "j.kryeziu06@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/jeta-kryeziu"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/jeta_cv_12_2024.pdf"
profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Extensive experience with spatial-sensor data and algorithm development.
- ✔️ Skilled in Python (FastAPI, Pandas, Numpy), SQL, DBT, and Airflow.
- ✔️ Experienced in visualizing and analyzing sensor data to deliver insights.
- ✔️ Proficient in PowerBI and interactive dashboard development.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: Python (FastAPI, Scikit-learn, Pandas), SQL, DBT
- 📊 Data Visualization: PowerBI, Streamlit
- 🗄️ Databases: Snowflake, AWS, PostgreSQL
- 🤖 Machine Learning: Neural networks, classification algorithms
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Data Scientist | TIVE Inc., Prishtina**")
    st.write("11/2023 - 11/2024")
    st.write(
        """
- ► Patrolled the premises to ensure safety and security.
- ► Monitored for any unusual activity and reported to the owner.
"""
    )

    # --- JOB 2
    st.write("\n")
    st.write("🚧", "House Cat")
    st.write("10/2021 - 08/2023")
    st.write(
        """
- ► Provided companionship and emotional support to the household.
- ► Maintained a clean and organized living space by using the litter box.
"""
    )



elif page == "About":
    st.title("About Me")
    st.write("""
Hi there! I'm Camazing CATie, a passionate and dedicated cat with a love for napping and purring. I have a knack for finding the purr-fect solution to any problem, whether it's finding the coziest spot in the house or catching that elusive toy. With my strong communication skills and agility, I'm always ready to provide companionship and support to those around me. When I'm not busy patrolling the premises or lounging in the sun, you can find me exploring new adventures and making new friends. Feel free to connect with me on LinkedIn or drop me an email – I'm always up for a chat about cats, napping techniques, or anything else that piques my interest!
""")

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")

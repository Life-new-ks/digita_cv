import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jeta Kryeziu"
PAGE_ICON = ":wave:"
NAME = "Camazing CATie"
DESCRIPTION = """
CATa SCATist specializing in Napping and Purring. With a knack for finding the purr-fect solution to any problem.
"""

EMAIL = "the_camazing_catie@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/catie-cata-123456789/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/cat_cv.pdf"
profile_pic_file = "assets/profile-pic.jpeg"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects"])

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
- ✔️ Protected the house from suspicious insects.
- ✔️ Improved human produc􀆟vity by si􀆫ng on laptops.
- ✔️ Monitored birds, cars, and neighbors.
- ✔️ Reported suspicious ac􀆟vity by staring intensely.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 🐾 Expert in napping techniques and finding the coziest spots.
- 🐾 Strong communica􀆟on skills: meow, louder meow, drama􀆟c meow
- 🐾 Skilled in hunting and catching toys, demonstrating agility and precision.
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "Security Assistant")
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


elif page == "Projects":
    st.title("Projects")
    st.write("\n")
    st.write("🐁The Great Mouse Patrol")
    st.write(
        "Monitored the house for suspicious mouse activity and completed nightly security checks.")

    st.write("\n")
    st.write("📍Sunbeam Location Tracker")
    st.write(
        "Identified the warmest sunny spots in the house and created an optimized daily nap schedule.")
    
    st.write("\n")
    st.write("📦Cardboard Box Quality Testing")
    st.write(
        "Tested boxes of different sizes for comfort, durability, and overall sitting potential.")

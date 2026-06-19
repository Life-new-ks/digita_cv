import streamlit as st
from PIL import Image
from config import PROFILE_PIC_FILE, RESUME_FILE, NAME, DESCRIPTION

PROFILE_PIC = Image.open(PROFILE_PIC_FILE)

with open(RESUME_FILE, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


col1, col2 = st.columns([1, 2], gap="small")

with col1:
    st.image(PROFILE_PIC, width=230)

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

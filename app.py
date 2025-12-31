import streamlit as st
from PIL import Image

st.set_page_config(page_title="Finance Portfolio", layout="wide")

# Title
st.title("📊 APS – Finance & Data Science Portfolio")

# Profile Image
img = Image.open("profile.jpg")
st.image(img, width=100)

# About
st.subheader("About Me")
st.write("""
I am a finance and data science enthusiast with skills in:
- Python
- Stock Market Analysis
- Machine Learning
- Power BI / Excel / Tableau
""")

# Resume Download
with open("resume.pdf", "rb") as file:
    st.download_button(
        label="📄 Download Resume",
        data=file,
        file_name="APS_Resume.pdf",
        mime="application/pdf"
    )

st.success("Use the sidebar to explore my work 🚀")

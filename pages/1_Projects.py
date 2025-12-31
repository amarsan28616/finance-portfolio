import streamlit as st

st.title("💼 Projects")

projects = [
    "📈 Stock Price Analysis using Python",
    "🤖 Machine Learning Stock Prediction",
    "📊 Finance Dashboard using Power BI",
    "🧮 Actuarial Math Projects (ACET)"
]

for p in projects:
    st.write("•", p)

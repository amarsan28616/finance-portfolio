import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Stock Analysis")

df = pd.read_csv("data/sample_stock.csv")
st.dataframe(df.head())

st.subheader("Closing Price Trend")

plt.figure()
plt.plot(df["Date"], df["Close"])
plt.xticks(rotation=45)
st.pyplot(plt)

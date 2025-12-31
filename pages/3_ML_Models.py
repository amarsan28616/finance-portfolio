import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🤖 Machine Learning Models")

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([100, 110, 120, 130, 140])

model = LinearRegression()
model.fit(X, y)

future_day = st.slider("Select Day", 6, 10)
prediction = model.predict([[future_day]])

st.write(f"📈 Predicted Price: **{prediction[0]:.2f}**")

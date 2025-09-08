import joblib
import streamlit as st
import numpy as np

FILE = "./regression.joblib"

model = joblib.load(FILE)

st.title("House Price Prediction")
size = st.number_input("Insert a size")
bedrooms = st.number_input("Insert a number of bedrooms")
garden = st.checkbox("Does the house have a garden")


def prediction(size, room, hasGarden):
    X_test = np.array([[size, room, hasGarden]])
    predict = model.predict(X_test)
    return predict[0]


t = prediction(size, bedrooms, garden)
st.write(f"The predicted price is {t:.2f}k$")

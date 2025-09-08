import joblib
import streamlit as st

FILE = "./regression.joblib"

data = joblib.load(FILE)

size = st.number_input("Insert a size")
bedrooms = st.number_input("Insert a number of bedrooms")
garden = st.checkbox("Does the house have a garden")

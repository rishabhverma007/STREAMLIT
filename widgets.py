import streamlit as st
import pandas as pd
import numpy as np
st.title("Streamlit Text Input")
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age} years.")

options = ["Python", "JavaScript", "Java", "C++"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}    
df = pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file is not None:
    df_uploaded = pd.read_csv(upload_file)
    st.write(df_uploaded)
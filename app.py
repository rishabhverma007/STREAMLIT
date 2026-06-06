import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Hello Streamlit")

#Display a simple text
st.write("This is a simple Streamlit app.")
# Create a simple DataFrame
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': [10, 20, 30, 40, 50],
})
# Display the DataFrame
st.write("Here is a simple DataFrame:")
st.write(df)

# Create a simple line chart
chart_data = pd.DataFrame(
    data = np.random.rand(1,20)
)
st.line_chart(chart_data)\


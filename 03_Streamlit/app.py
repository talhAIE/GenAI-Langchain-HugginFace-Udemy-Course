import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Streamlit App")

# display a sample text
st.write("This is a sample Streamlit app.")

# create a sample dataframe

df=pd.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "B": [10, 20, 30, 40, 50],
        "C": [100, 200, 300, 400, 500],
    }
)

# display the dataframe
st.write("Sample DataFrame:")
# st.dataframe(df)

st.write(df)

# Create a line chart

data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)

st.line_chart(data)
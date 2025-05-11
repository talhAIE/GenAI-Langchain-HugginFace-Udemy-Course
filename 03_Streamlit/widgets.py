import streamlit as st
import pandas as pd
import numpy as np

# title
st.title("Streamlit Widgets")

user_name=st.text_input("Enter your name")

st.write(f"Your Age is {st.slider('select a age',0,100,25)}")
choice=st.selectbox("Select your choice",['python','java','c++'])
st.write(f"Your choice is {choice}")

if user_name:
    st.write(f"Hello {user_name}")

df=pd.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "B": [10, 20, 30, 40, 50],
        "C": [100, 200, 300, 400, 500],
    }
)

# display the dataframe
st.write("Sample DataFrame:")
df.to_csv("sample.csv")
st.write(df)
# st.dataframe(df)

# file uploader

file_upload=st.file_uploader("Upload a file",type="csv")

if file_upload is not None:
    df=pd.read_csv(file_upload)
    st.write(df)

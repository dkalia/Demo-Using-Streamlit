import streamlit as st
import pandas as pd

st.title("Demo Dashboard")
st.write("Example dashboard to Marquee class for Queen's University")

#st.write is similar to print() in python
categories = ['a', 'b', 'c']
st.multiselect("pick an option", categories)

st.sidebar.button("Click me!")

url = "https://www.iposcoop.com/last-100-ipos/"
df = pd.read_html(url)[0]

st.write(df)

st.dataframe(df)


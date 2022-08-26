import streamlit as st
import pandas as pd

st.title("Demo Dashboard")
st.write("Example dashboard to Marquee class for Queen's University")


categories = ['a', 'b', 'c']
st.multiselect("pick an option", categories)

st.sidebar.button("Click me!")



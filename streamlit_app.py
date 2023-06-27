import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

data = pd.read_csv("data.csv")
st.plotly_chart(data["amount"])
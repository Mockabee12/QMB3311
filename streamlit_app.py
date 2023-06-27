import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

data = pd.read_csv("17_Optimization/credit_data.csv")
st.bar_chart(data["amount"])
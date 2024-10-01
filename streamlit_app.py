import streamlit as st
import pandas as pd

st.title('Cricket Analysis app for EDA')

st.write('Hello world!')

df = pd.read_csv('https://raw.githubusercontent.com/XyeD97/task3-ml/refs/heads/master/ODI_Match_info.csv')

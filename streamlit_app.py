import streamlit as st
import pandas as pd

st.title('Cricket Analysis app for EDA')

st.info('This app builds a machine learning model on cricket related dataset')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/XyeD97/task3-ml/refs/heads/master/ODI_Match_info.csv')
  df

  st.write('**X**')
  x = df.drop('id', axis=1)
  x

  st.write('**Y**')
  y = df.id
  y
with st.expander('Data Visualization'):
  st.scatter_chart(data= df, x='team1', y= 'team2', color='toss_winner')

#Data preparations
with st.sidebar:
  st.header('Input features')

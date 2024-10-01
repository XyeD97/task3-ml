import streamlit as st
import pandas as pd

st.title('Cricket Analysis app for EDA')

st.info('This app builds a machine learning model on cricket related dataset')

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/XyeD97/task3-ml/refs/heads/master/ODI_Match_info.csv')

with st.expander('Data'):
    st.write('**Raw Data**')
    st.write(df)

    st.write('**X**')
    x = df.drop('id', axis=1)
    st.write(x)

    st.write('**Y**')
    y = df.id
    st.write(y)

with st.expander('Data Visualization'):
    st.scatter_chart(data=df, x='team1', y='team2', color='toss_winner')

# Data preparation and sidebar setup
with st.sidebar:
    st.header('Input features')

    # Combine team1 and team2 columns to form a unique list of countries
    all_teams = pd.concat([df['team1'], df['team2']]).drop_duplicates().sort_values()

    # Select box for Team 1
    team1 = st.selectbox("Select Your Team", all_teams)

    # Select box for Team 2
    team2 = st.selectbox("Select Opposite Team", all_teams)

    # Select box for Venue
    venue = st.selectbox("Select Venue", df['venue'].drop_duplicates().sort_values())

    # Add a button for analysis
    if st.button("Analyze"):
        # Display the selected options
        st.write(f"Analyzing match between {team1} and {team2} at {venue}")

        # You can perform any analysis based on the selected teams and venue

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/XyeD97/task3-ml/refs/heads/master/ODI_Match_info.csv')

# Show the dataset in Streamlit
st.write("Dataset Overview", df.head())

# 1. Data Overview
st.write("Summary Statistics")

st.write(df.describe())  # Statistical summary of numerical columns

# 2. Check for missing values
st.write("Missing Values")

st.write(df.isnull().sum())  # Check which columns have missing values

# 3. Plotting some key visualizations

# 4. Distribution of matches played per venue
st.write("Matches Played at Different Venues")

plt.figure(figsize=(10, 5))


sns.countplot(y=df['venue'], order=df['venue'].value_counts().index)

plt.title('Matches Played by Venue')

st.pyplot()

# 5. Number of wins by team
st.write("Wins by Team")
plt.figure(figsize=(10, 5))

sns.countplot(x=df['winner'], order=df['winner'].value_counts().index)
plt.title('Number of Wins by Team')
plt.xticks(rotation=90)
st.pyplot()

# 6. Wins by toss decision (field or bat)
st.write("Wins Based on Toss Decision")
plt.figure(figsize=(6, 4))

sns.countplot(x=df['toss_decision'], hue=df['winner'])
plt.title('Wins Based on Toss Decision')
st.pyplot()

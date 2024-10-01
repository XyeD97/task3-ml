import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/XyeD97/task3-ml/refs/heads/master/ODI_Match_info.csv')

# Sidebar for plot selection
st.sidebar.title("Visualization Options")
plot_selection = st.sidebar.selectbox(
    "Select the visualization type:",
    ("Dataset Overview", "Summary Statistics", "Missing Values", "Matches Played at Different Venues", "Wins by Team", "Wins by Toss Decision")
)

# Show the dataset in Streamlit
if plot_selection == "Dataset Overview":
    st.write("### Dataset Overview")
    st.write(df.head())

# 1. Data Overview
if plot_selection == "Summary Statistics":
    st.write("### Summary Statistics")
    st.write(df.describe())  # Statistical summary of numerical columns

# 2. Check for missing values
if plot_selection == "Missing Values":
    st.write("### Missing Values")
    st.write(df.isnull().sum())  # Check which columns have missing values

# 4. Distribution of matches played per venue
if plot_selection == "Matches Played at Different Venues":
    st.write("### Matches Played at Different Venues")

    # Limiting the plot to the top 20 venues with the most matches
    top_venues = df['venue'].value_counts().nlargest(20)

    plt.figure(figsize=(15, 10))  # Adjust size for better readability
    sns.barplot(y=top_venues.index, x=top_venues.values, palette="coolwarm")

    # Updating the title, labels, and adjusting font sizes
    plt.title('Top 20 Venues by Matches Played', fontsize=18)
    plt.xlabel('Number of Matches Played', fontsize=14)
    plt.ylabel('Venue', fontsize=14)

    # Adjust the y-axis tick label font size for better readability
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Apply tight layout to avoid label overlap
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot()

# 5. Number of wins by team
if plot_selection == "Wins by Team":
    st.write("### Wins by Team")
    plt.figure(figsize=(10, 5))
    sns.countplot(x=df['winner'], order=df['winner'].value_counts().index)
    plt.title('Number of Wins by Team')
    plt.xticks(rotation=90)
    st.pyplot()

# 6. Wins by toss decision (field or bat)
if plot_selection == "Wins by Toss Decision":
    st.write("### Wins Based on Toss Decision")
    plt.figure(figsize=(30, 20))
    sns.countplot(x=df['toss_decision'], hue=df['winner'])
    plt.title('Wins Based on Toss Decision')
    st.pyplot()

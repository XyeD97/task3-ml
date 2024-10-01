import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/XyeD97/task3-ml/refs/heads/master/ODI_Match_info.csv')

# Sidebar for selecting visualizations
st.sidebar.title("Visualization Selector")
plot_type = st.sidebar.selectbox(
    "Choose a plot to display",
    ("Dataset Overview", "Summary Statistics", "Missing Values", 
     "Matches Played at Different Venues", "Wins by Team", 
     "Wins Based on Toss Decision")
)

# Title for the Streamlit app
st.title("ODI Match Information Visualization")

# Show the selected visualization
if plot_type == "Dataset Overview":
    st.write("### Dataset Overview")
    st.write(df.head())

elif plot_type == "Summary Statistics":
    st.write("### Summary Statistics")
    st.write(df.describe())

elif plot_type == "Missing Values":
    st.write("### Missing Values")
    st.write(df.isnull().sum())

elif plot_type == "Matches Played at Different Venues":
    st.write("### Matches Played at Different Venues")
    plt.figure(figsize=(40, 30))  # Adjusted size for better display
    sns.countplot(y=df['venue'], order=df['venue'].value_counts().index, palette="coolwarm")
    plt.title('Matches Played by Venue', fontsize=42)
    plt.xlabel('Matches Played', fontsize=36)
    plt.ylabel('Venue', fontsize=36)
    st.pyplot()

elif plot_type == "Wins by Team":
    st.write("### Wins by Team")
    plt.figure(figsize=(15, 8))  # Adjusted size for better display
    sns.countplot(x=df['winner'], order=df['winner'].value_counts().index, palette="Blues_d")
    plt.title('Number of Wins by Team', fontsize=16)
    plt.xticks(rotation=90, fontsize=10)
    plt.xlabel('Team', fontsize=12)
    plt.ylabel('Wins', fontsize=12)
    st.pyplot()

elif plot_type == "Wins Based on Toss Decision":
    st.write("### Wins Based on Toss Decision")
    plt.figure(figsize=(30, 15))  # Adjusted size for better display
    sns.countplot(x=df['toss_decision'], hue=df['winner'], palette="Set2")
    plt.title('Wins Based on Toss Decision', fontsize=42)
    plt.xlabel('Toss Decision', fontsize=36)
    plt.ylabel('Count', fontsize=36)
    st.pyplot()

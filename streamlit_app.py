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
    
    # Add a slider to allow users to select the number of top venues to display
    top_n_venues = st.sidebar.slider("Select number of top venues to display", 5, 50, 20)
    
    # Limiting the plot to the top N venues with the most matches
    top_venues = df['venue'].value_counts().nlargest(top_n_venues)

    plt.figure(figsize=(15, 10))  # Adjust size for better readability
    sns.barplot(y=top_venues.index, x=top_venues.values, palette="coolwarm")

    # Updating the title, labels, and adjusting font sizes
    plt.title(f'Top {top_n_venues} Venues by Matches Played', fontsize=18)
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

    # Allow the user to filter the top N teams by number of wins
    top_n_teams = st.sidebar.slider("Select number of top teams to display", 5, 20, 10)

    # Filter and plot the top N teams by number of wins
    top_winning_teams = df['winner'].value_counts().nlargest(top_n_teams).index
    filtered_df = df[df['winner'].isin(top_winning_teams)]

    plt.figure(figsize=(10, 5))
    sns.countplot(x=filtered_df['winner'], order=filtered_df['winner'].value_counts().index)
    plt.title(f'Number of Wins by Top {top_n_teams} Teams')
    plt.xticks(rotation=90)
    st.pyplot()

# 6. Wins by toss decision (field or bat)
if plot_selection == "Wins by Toss Decision":
    st.write("### Wins Based on Toss Decision")

    # Provide an option for the user to filter by toss decision
    toss_decision_filter = st.sidebar.multiselect(
        "Filter by Toss Decision", df['toss_decision'].unique(), default=df['toss_decision'].unique()
    )
    
    filtered_df = df[df['toss_decision'].isin(toss_decision_filter)]

    plt.figure(figsize=(30, 20))
    sns.countplot(x=filtered_df['toss_decision'], hue=filtered_df['winner'])
    plt.title('Wins Based on Toss Decision')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    st.pyplot()

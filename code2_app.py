import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data (assuming df is your DataFrame)
# df = pd.read_csv('your_dataset.csv')

# Sidebar and Selectbox for choosing plot type
st.sidebar.title("Plot Options")

# Create a selectbox to choose the data to visualize
plot_option = st.sidebar.selectbox(
    'Select the metric to visualize:',
    ('Matches Played', 'Wins by Team')
)

# Set the style and color palette
sns.set_style("whitegrid")  # Change this to 'darkgrid', 'white', 'dark', or 'ticks' if you prefer
sns.set_palette("Blues_r")  # Choose a Seaborn color palette for the bars

# Create a larger figure for better readability
plt.figure(figsize=(15, 10))

# Dynamically plot the selected option
if plot_option == 'Matches Played':
    sns.barplot(data=df, x='Matches Played', y='Venue', orient='h')
    plt.title('Matches Played at Different Venues', fontsize=16)
    plt.xlabel('Matches', fontsize=12)
    plt.ylabel('Venues', fontsize=12)
elif plot_option == 'Wins by Team':
    sns.barplot(data=df, x='Wins', y='Team', orient='h')
    plt.title('Wins by Different Teams', fontsize=16)
    plt.xlabel('Wins', fontsize=12)
    plt.ylabel('Teams', fontsize=12)

# Rotate x-axis labels and adjust the alignment
plt.xticks(rotation=45, ha='right')

# Dis

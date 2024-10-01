import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/XyeD97/task3-ml/refs/heads/master/ODI_Match_info.csv') 

# Sidebar for plot options
st.sidebar.title("Plot Options")

# Selectbox for choosing the data to visualize
plot_option = st.sidebar.selectbox(
    'Select the metric to visualize:',
    ('Matches Played', 'Wins by Team')
)

# Set Seaborn style and color palette
sns.set_style("whitegrid")  # Choose 'whitegrid' for the background
sns.set_palette("Blues_r")  # Blue color palette, you can change it to any other

# Create a larger figure for better readability
plt.figure(figsize=(15, 10))

# Dynamically plot based on user selection from the sidebar
if plot_option == 'Matches Played':
    # Ensure the column names are correct
    if 'Matches Played' in df.columns and 'Venue' in df.columns:
        sns.barplot(data=df, x='Matches Played', y='Venue', orient='h')
        plt.title('Matches Played at Different Venues', fontsize=16)
        plt.xlabel('Matches', fontsize=12)
        plt.ylabel('Venues', fontsize=12)
    else:
        st.error("Columns 'Matches Played' or 'Venue' not found in dataset.")
elif plot_option == 'Wins by Team':
    if 'Wins' in df.columns and 'Team' in df.columns:
        sns.barplot(data=df, x='Wins', y='Team', orient='h')
        plt.title('Wins by Different Teams', fontsize=16)
        plt.xlabel('Wins', fontsize=12)
        plt.ylabel('Teams', fontsize=12)
    else:
        st.error("Columns 'Wins' or 'Team' not found in dataset.")

# Rotate x-axis labels and adjust alignment
plt.xticks(rotation=45, ha='right')

# Display the plot using Streamlit
st.pyplot(plt)

# Optional: Add a custom sidebar for further input or customization options if needed
st.sidebar.markdown("### Customize your plot")

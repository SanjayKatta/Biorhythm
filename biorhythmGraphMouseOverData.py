# streamlit run biorhythmGraphMouseOverData.py

import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import plotly.express as px

# Function to calculate biorhythm values
def calculate_biorhythm(birthdate, start_date, end_date):
    # Convert birthdate to string format
    birthdate_str = birthdate.strftime("%Y-%m-%d")

    # Initialize lists to store data
    dates = []
    physical_data = []
    emotional_data = []
    intellectual_data = []

    # Loop through each day in the period
    current_date = start_date
    while current_date <= end_date:
        # Calculate the value of each cycle for the current day
        days_since_birth = (current_date - birthdate).days
        physical = np.sin(2 * np.pi * days_since_birth / 23) * 10
        emotional = np.sin(2 * np.pi * days_since_birth / 28) * 10
        intellectual = np.sin(2 * np.pi * days_since_birth / 33) * 10

        # Add the data to the respective lists
        dates.append(current_date)
        physical_data.append(physical)
        emotional_data.append(emotional)
        intellectual_data.append(intellectual)

        # Move to the next day
        current_date += dt.timedelta(days=1)

    return dates, physical_data, emotional_data, intellectual_data

# Streamlit app
st.title("Biorhythm Graph")

# User input for birthdate and date range in sidebar
birthdate = st.sidebar.date_input("Enter your birthdate")
start_date = st.sidebar.date_input("Enter the start date")
end_date = st.sidebar.date_input("Enter the end date")

# Check if the user has entered valid dates
if birthdate > start_date:
    st.error("Error: Birthdate cannot be after the start date.")
elif start_date > end_date:
    st.error("Error: Start date cannot be after the end date.")
else:
    # Calculate biorhythm values
    dates, physical_data, emotional_data, intellectual_data = calculate_biorhythm(birthdate, start_date, end_date)

    # Create a DataFrame from the data
    data = pd.DataFrame({
        "Date": dates,
        "Physical": physical_data,
        "Emotional": emotional_data,
        "Intellectual": intellectual_data
    })

    # Plot the biorhythm graph using Plotly
    fig = px.line(data, x="Date", y=["Physical", "Emotional", "Intellectual"])
    fig.update_traces(hovertemplate="Date: %{x}<br>Value: %{y}")
    fig.update_layout(
        title="Biorhythm Graph",
        xaxis_title="Date",
        yaxis_title="Value"
    )
    st.plotly_chart(fig)

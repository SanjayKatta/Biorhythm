import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

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

# User input for birthdate and date range
birthdate = st.date_input("Enter your birthdate")
start_date = st.date_input("Enter the start date")
end_date = st.date_input("Enter the end date")

# Calculate biorhythm values
dates, physical_data, emotional_data, intellectual_data = calculate_biorhythm(birthdate, start_date, end_date)

# Create a DataFrame from the data
data = pd.DataFrame({
    "Date": dates,
    "Physical": physical_data,
    "Emotional": emotional_data,
    "Intellectual": intellectual_data
})

# Display the DataFrame
st.dataframe(data)

# Plot the biorhythm graph
fig, ax = plt.subplots()
ax.plot(data["Date"], data["Physical"], label="Physical", color="red")
ax.plot(data["Date"], data["Emotional"], label="Emotional", color="blue")
ax.plot(data["Date"], data["Intellectual"], label="Intellectual", color="green")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.set_title("Biorhythm Graph")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)
import streamlit as st
import pandas as pd

# Page title
st.title("📊 Crypto Prices Dashboard")

# Load the CSV file
df = pd.read_csv("crypto_prices.csv")

# Display the data as a table
st.subheader("Data from CSV File")
st.dataframe(df)

# Show basic statistics
st.subheader("Descriptive Statistics")
st.write(df.describe())

# Create a line chart for the 'Close' prices

# Page title
st.title("📊 Crypto Prices Dashboard")

# Load CSV
df = pd.read_csv("crypto_prices.csv")

# Convert 'date' column to datetime
#df["date"] = pd.to_datetime(df["date"]).dt.date

# Sort data by date
#df = df.sort_values("date")

# Display table
st.subheader("Table: Crypto Prices Over Time")
st.dataframe(df)

# Line chart
st.subheader("Line Chart: Open and Close Prices Over Time")
st.line_chart(df.set_index("date")[["open", "close"]])

# Optional: Show statistics
st.subheader("Descriptive Statistics")
st.write(df[["open", "close"]].describe())



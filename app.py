import streamlit as st
import pandas as pd

# Set the title of your web dashboard
st.title("Smart Expense Tracker & Analyzer")

# Load your dataset
df = pd.read_csv("data/expense.csv")

# Display the data as an interactive table on the webpage
st.subheader("My Expense Records")
st.dataframe(df)

# Calculate and display a financial metric card
total_spent = df['amount'].sum()
st.metric(label="Total Money Spent", value=f"₹ {total_spent}")
# group data by category for ou chart
category_df = df.groupby("category")["amount"].sum()
# display a subheader and the bar chart
st.subheader("spending by category")
st.bar_chart(category_df)

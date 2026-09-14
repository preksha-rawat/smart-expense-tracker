# Smart Expense Tracker

A Python-based web application I built to help track daily expenses, manage monthly budgets, and analyze spending habits.

**Live Demo:** [Preksha's Expense Tracker](https://preksha-smart-expense-tracker.streamlit.app)

## Project Overview
I developed this tool to make personal finance tracking simple and visual. Instead of using complex spreadsheets, this app provides a clean interface to log expenses, check budget limits, and see exactly where money is going each month.

## Key Features
* **Easy Expense Logging:** Users can quickly add expenses by date, category, and amount. The table automatically organizes everything so the most recent entries always stay at the top.
* **Monthly Filtering:** You can select specific months from a dropdown menu to filter your records and focus only on that month's spending.
* **Budget Tracking:** The app allows you to set a custom budget for the month and gives an immediate alert if your total spending crosses that limit.
* **Visual Breakdown:** It takes the raw expense data and automatically generates bar charts, making it easy to see which categories (like travel or food) are taking up the most money.
* **Smart Insights:** The app calculates your highest spending category and provides simple, data-driven advice on where to cut back to save money.

## Technologies Used
* **Python:** Core programming language used for all backend logic.
* **Streamlit:** Used to build the frontend user interface and handle live updates.
* **Pandas:** Used for formatting, filtering, and sorting the tabular data.

## How to Run Locally
1. Clone this repository to your local machine.
2. Install the required libraries using: `pip install -r requirements.txt`
3. Start the application by running: `streamlit run app.py`
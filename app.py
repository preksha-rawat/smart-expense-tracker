# Import the Pandas library and give it a short nickname 'pd'
import pandas as pd

print("--- Reading Data with Pandas ---")

# Tell Pandas to read your exact file and store it in a DataFrame variable named 'df'
df = pd.read_csv("data/expense.csv")

# Print the entire DataFrame to the screen
print(df)
# select just the 'amount' column and calculate the sum
total_spent = df['amount'].sum()
#print the final total to the sceen
print("\n--- spending analysis ---")
print("total spent: ₹", total_spent)
# Group by category and sum the amounts
category_spending = df.groupby('category')['amount'].sum()

# Print the category breakdown
print("\n--- Spending by Category ---")
print(category_spending)
# Find the largest number in the amount column
highest_expense = df['amount'].max()

print("\n--- Quick Insights ---")
print("Highest single expense: ₹", highest_expense)
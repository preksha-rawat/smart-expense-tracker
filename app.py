# Import the Pandas library and give it a short nickname 'pd'
import pandas as pd

print("--- Reading Data with Pandas ---")

# Tell Pandas to read your exact file and store it in a DataFrame variable named 'df'
df = pd.read_csv("data/expense.csv")

# Print the entire DataFrame to the screen
print(df)
import streamlit as st
import pandas as pd

st.title("Smart Expense Tracker & Analyzer")
st.write("Easily track your expenses, visualize your spending patterns, and stay within your budget.")

# Initialize an empty list or session state to hold expenses dynamically
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Section 1: Manual Expense Input Form
st.subheader("➕ Add a New Expense")
with st.form("expense_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        expense_date = st.date_input("Date")
    with col2:
        expense_category = st.text_input("Category (e.g., Food, Travel)")
    with col3:
        expense_amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
    
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        if expense_category.strip() == "":
            st.warning("Please enter a valid category.")
        else:
            st.session_state.expenses.append({
                "date": str(expense_date),
                "category": expense_category.strip().lower(),
                "amount": float(expense_amount)
            })
            st.success("Expense added successfully!")

# Convert session expenses into a DataFrame
if len(st.session_state.expenses) > 0:
    df = pd.DataFrame(st.session_state.expenses)
    
    # Section 2: Display Expense Records Table
    st.subheader("📊 Your Expense Records")
    st.dataframe(df, use_container_width=True)
    
    # Section 3: Financial Summary & Metrics
    total_spent = df['amount'].sum()
    st.metric(label="Total Money Spent", value=f"₹ {total_spent}")
    
    # Section 4: Budget Management
    monthly_budget = st.number_input("Set Your Monthly Budget Limit (₹)", min_value=0.0, value=5000.0, step=500.0)
    
    if total_spent > monthly_budget:
        st.error(f"⚠️ Budget Alert: You have exceeded your budget by ₹ {total_spent - monthly_budget}!")
    else:
        st.success(f"✅ Great job! You are within your budget. Remaining: ₹ {monthly_budget - total_spent}")
        
    # Section 5: Spending by Category Chart
    st.subheader("📈 Spending by Category")
    category_df = df.groupby("category")["amount"].sum()
    st.bar_chart(category_df)
    
    # Section 6: Automated Insights / Advice
    st.subheader("💡 Smart Financial Advice")
    highest_category = category_df.idxmax()
    highest_amount = category_df.max()
    st.info(f"You are spending the most on **{highest_category}** (₹ {highest_amount}). Consider setting a specific sub-budget for this category to save more effectively.")

else:
    st.info("👈 Fill out the form above and click 'Add Expense' to start building your dashboard!")
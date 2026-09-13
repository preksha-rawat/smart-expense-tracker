import streamlit as st
import pandas as pd
import datetime

st.title("Smart Expense Tracker & Analyzer")
st.write("Easily track your expenses, visualize your spending patterns, and stay within your budget.")

# Initialize session state to hold expenses dynamically
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Keep track of the last used date so it doesn't default back annoyingly
if "last_date" not in st.session_state:
    st.session_state.last_date = datetime.date.today()

# Section 1: Manual Expense Input Form
st.subheader("➕ Add a New Expense")
with st.form("expense_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        expense_date = st.date_input("Date", value=st.session_state.last_date)
    with col2:
        expense_category = st.text_input("Category (e.g., Food, Travel)")
    with col3:
        expense_amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
    
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        if expense_category.strip() == "":
            st.warning("Please enter a valid category.")
        else:
            # Save the date they just used so it persists
            st.session_state.last_date = expense_date
            st.session_state.expenses.append({
                "date": pd.to_datetime(expense_date),
                "category": expense_category.strip().lower(),
                "amount": float(expense_amount)
            })
            st.success("Expense added successfully!")
            st.rerun()

# Convert session expenses into a DataFrame if data exists
if len(st.session_state.expenses) > 0:
    df = pd.DataFrame(st.session_state.expenses)
    
    # Sort dataframe by date in descending order (newest/most recent first)
    df = df.sort_values(by="date", ascending=False).reset_index(drop=True)
    
    # Extract Month-Year for filtering (e.g., "September 2026")
    df['Month-Year'] = df['date'].dt.strftime('%B %Y')
    
    # Section 2: Monthly Filter Dropdown
    st.subheader("📅 Filter by Month")
    available_months = df['Month-Year'].unique()
    selected_month = st.selectbox("Select Month", available_months)
    
    # Filter dataframe based on selected month
    filtered_df = df[df['Month-Year'] == selected_month]
    
    # Format date nicely for display (YYYY-MM-DD)
    display_df = filtered_df.copy()
    display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
    
    # Section 3: Display Expense Records Table for that Month
    st.subheader(f"📊 Expense Records for {selected_month}")
    st.dataframe(display_df.drop(columns=['Month-Year']), use_container_width=True)
    
    # Section 4: Financial Summary & Metrics
    total_spent = filtered_df['amount'].sum()
    st.metric(label=f"Total Money Spent in {selected_month}", value=f"₹ {total_spent}")
    
    # Section 5: Budget Management
    monthly_budget = st.number_input(f"Set Monthly Budget for {selected_month} (₹)", min_value=0.0, value=5000.0, step=500.0)
    
    if total_spent > monthly_budget:
        st.error(f"⚠️ Budget Alert: You have exceeded your {selected_month} budget by ₹ {total_spent - monthly_budget}!")
    else:
        st.success(f"✅ Great job! You are within your budget for {selected_month}. Remaining: ₹ {monthly_budget - total_spent}")
        
    # Section 6: Spending by Category Chart
    st.subheader("📈 Spending by Category")
    if not filtered_df.empty:
        category_df = filtered_df.groupby("category")["amount"].sum()
        st.bar_chart(category_df)
        
        # Section 7: Automated Insights / Advice
        highest_category = category_df.idxmax()
        highest_amount = category_df.max()
        st.info(f"In {selected_month}, you are spending the most on **{highest_category}** (₹ {highest_amount}). Consider setting a specific sub-budget for this category.")

        # Section 8: AI Financial Advisor Integration
        st.subheader("🤖 AI Financial Advisor")
        st.write("Get personalized, AI-driven recommendations based on your current month's data.")

        if st.button("Generate AI Financial Advice"):
            st.success("Analysis Complete!")
            st.markdown(f"""
            ### 📊 Professional AI Assessment for {selected_month}
            - **Spending Health:** You recorded transactions across **{len(filtered_df['category'].unique())}** unique categories with a total outflow of **₹ {total_spent}**.
            - **Primary Cost Driver:** Your largest capital allocation is toward **{highest_category}** totaling **₹ {highest_amount}** ({round((highest_amount/total_spent)*100, 1)}% of total spend).
            - **Actionable Recommendation:** To optimize your financial standing for {selected_month}, cap your discretionary spending in **{highest_category}** by 15% and redirect those funds into savings.
            """)
    else:
        st.info("No expenses recorded for this month yet.")

else:
    st.info("👈 Fill out the form above and click 'Add Expense' to start building your dashboard!")
""" Expense Tracker """
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Expense Tracker",
                   page_icon="👛",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   )

st.markdown("""
# Expense Tracker 👛🧾💵💳
This Web-App help you manange your expense in daily life by providing infomation such as pie chart graph etc. below.
""")
expenses_df = pd.DataFrame(columns = ["Expense","Method","Recipent", "Details", "Date", "Amount"])

method_bank_or_cash = ["Online Banking","Cash"]
config = {
    "Expense" :st.column_config.TextColumn("Expense", required = True),
    "Method" :st.column_config.SelectboxColumn("Method", options = method_bank_or_cash, required = True),
    "Recipent" :st.column_config.TextColumn("Recipent", required = True),
    "Details" :st.column_config.TextColumn("Detail"),
    "Date" :st.column_config.DatetimeColumn(format = "DD MMM YY, hh:mm", required = True),
    "Amount" :st.column_config.NumberColumn("Amount", format ="%d THB", required = True)
}

edit_expense_df = st.data_editor(expenses_df, column_config = config, num_rows="dynamic", use_container_width = True)

if st.button("Apply"):
    st.area_chart(expenses_df, x="Recipent", y="Expense", color=["#E8A09A"])




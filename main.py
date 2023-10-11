""" Expense Tracker """
import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# Page Config
st.set_page_config(page_title="Expense Tracker",
                   page_icon="👛",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   )
# Header
st.markdown("""
# Expense Tracker 👛🧾💵💳
This Web-App help you manange your expense in daily life by providing infomation such as pie chart graph etc. below.
""")

# Sidebar
st.sidebar.header("Upload CSV 🧾")
uploaded_file = st.sidebar.file_uploader("Upload .CSV File Here 👇", type=["csv"])

if uploaded_file is not None:
    try:
        uploaded_df = pd.read_csv(uploaded_file)
        # Convert the "Date" column to datetime format
        if 'Date' in uploaded_df.columns:
            uploaded_df['Date'] = pd.to_datetime(uploaded_df['Date'])
            
        st.sidebar.subheader("Uploaded CSV Data:")
        st.sidebar.write(uploaded_df)
        
        if st.sidebar.button("Apply Uploaded Data"):
            st.session_state.data_editor = uploaded_df.copy()
            st.success("Uploaded data applied successfully.")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

st.sidebar.markdown("""---""")

if "data_editor" not in st.session_state:
    st.session_state.data_editor = pd.DataFrame(columns=["Expense", "Method", "Type", "Details", "Date", "Amount"])
expenses_df = st.session_state.data_editor

method_bank_or_cash = ["Online Banking","Cash"]
config = {
    "Expense" :st.column_config.TextColumn("Expense", required = True),
    "Method" :st.column_config.SelectboxColumn("Method", options = method_bank_or_cash, required = True),
    "Type" :st.column_config.TextColumn("Type", required = True),
    "Details" :st.column_config.TextColumn("Detail"),
    "Date" :st.column_config.DateColumn(format="DD MMM YY", required = True),
    "Amount" :st.column_config.NumberColumn("Amount", format ="%d THB", required = True)
}

edit_expense_df = st.data_editor(expenses_df, column_config = config, num_rows="dynamic", use_container_width = True)

# Remove Blank with - in Details Column
edit_expense_df["Details"].fillna("-", inplace=True)

# Sidebar 2
st.sidebar.header("Download CSV 📥")
st.sidebar.markdown("""Export the dataframe as a csv or excel file here 👇.""")
st.sidebar.download_button("Download dataframe", convert_df(edit_expense_df), "expense_report.csv", "text/csv", use_container_width=True)
st.sidebar.markdown("""---""")

col1, col2 = st.columns(2)
with col1:
   st.header("Bar_Chart")
   st.bar_chart(edit_expense_df, x = "Type", y = "Amount")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
import streamlit as st
import pandas as pd
from app_model.it_tickets import get_all_it_tickets
from app_model.db import get_connection

st.set_page_config(
    page_title="It Tickets",
    page_icon="📋",
    layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard!")

    if st.button("Go to login page"):
        st.session_state['logged_in'] = False
        st.switch_page("Home.py")
    st.stop()

else:
    st.success("You are logged in!")


connection = get_connection()
data = get_all_it_tickets(connection)


st.title("Welcome to the It Tickets Dashboard 💻")

with st.sidebar:
    st.header("Navigation")
    priority_ = st.selectbox('Priority Level:', ["All"] + data['priority'].dropna().unique().tolist())


filtered_data = data[data['priority'] == priority_]

if priority_ == "All":
    filtered_data = data
else:
    filtered_data = data[data["priority"] == priority_]



tickets_total = len(data)
num_of_support_staff = data["assigned_to"].nunique()
resolved_tickets = (data["status"] == "Resolved").sum()
avg_resolution_time = data["resolution_time_hours"].mean()

st.subheader("📊 Quick Overview:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tickets:", tickets_total)

with col2:
    st.metric("Number of support staff:", num_of_support_staff)

with col3:
    st.metric("Resolved Tickets:", resolved_tickets)

with col4:
    st.metric("Average Resolution time:", avg_resolution_time)


col1, col3 = st.columns(2)

with col1:
    st.header(f"Ticket Priority: {priority_}")
    st.bar_chart(filtered_data['status'].value_counts())

with col3:
    st.subheader("Support given overview:")
    st.line_chart(filtered_data, x='status', y='assigned_to')


st.subheader("Filtered Data:")
st.dataframe(filtered_data)
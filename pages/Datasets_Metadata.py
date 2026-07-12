import streamlit as st
import pandas as pd
from app_model.metadatas import get_all_datasets_metadata
from app_model.db import get_connection

st.set_page_config(
    page_title="Datasets Metadata",
    page_icon="📂",
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
data = get_all_datasets_metadata(connection)


st.title("Welcome to the Datasets Dashboard 💻")


with st.sidebar:
    st.header("Navigation")
    uploader_ = st.selectbox('Uploaded By:',["All"] + data["uploaded_by"].dropna().unique().tolist()) #use of ai to debug

filtered_data = data[data["uploaded_by"] == uploader_]

if uploader_ == "All":
    filtered_data = data
else:
    filtered_data = data[data["uploaded_by"] == uploader_]


#use of AI to understand .nunique (to display the number of uploaders) and st.metric
datasets_total = len(data)
records_total = data["rows"].sum()
total_uploaders = data["uploaded_by"].nunique()
latest_uploads = data["upload_date"].max()

st.subheader("📊 Quick Overview:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Datasets: ", datasets_total)

with col2:
    st.metric("Total Records: ", records_total)

with col3:
    st.metric("Total uploaders: ", total_uploaders)

with col4:
    st.metric("Latest Upload: ", latest_uploads)


st.subheader("Filtered Data:")
st.dataframe(filtered_data)
import streamlit as st
from show_predict_page import show_predict_page
from show_raw_data import show_raw_data

view_data = st.checkbox('View Raw Data', value=False)

if view_data:
    show_raw_data()
else:
    show_predict_page()
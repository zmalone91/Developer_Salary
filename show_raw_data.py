import streamlit as st
import pandas as pd

def show_raw_data():
    df = pd.read_csv('stackoverflow_df_final.csv')
    
    st.write(df)
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("personality_synthetic_dataset.csv")
    return df

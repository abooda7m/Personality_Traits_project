import streamlit as st
from data.data_loader import load_data
import tabs.data_overview as data_overview
import tabs.categorical_analysis as categorical
import tabs.numerical_analysis as numerical
import tabs.prediction as prediction
import landingPage


st.set_page_config(page_title="Personality Classification App", layout="wide")

df = load_data()

tabs = {
    "📊 Data Overview": data_overview,
    "🧩 Categorical Analysis": categorical,
    "🔢 Numerical Analysis": numerical,
    "🤖 Prediction": prediction,
}

selected = st.sidebar.radio("Go to", list(tabs.keys()))

tabs[selected].show(df)

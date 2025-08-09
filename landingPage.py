import streamlit as st
from data.data_loader import load_data
from tabs import (
    data_overview,
    categorical_analysis,
    numerical_analysis,
    prediction
)

st.set_page_config(page_title="Personality Dashboard", layout="wide")
st.title("Personality Traits Classification Dashboard")

with st.spinner("Loading data..."):
    df = load_data()

tab1, tab2, tab3, tab4 = st.tabs([
    " Data Overview",
    " Categorical Analysis",
    " Numerical Analysis",
    " Personality Prediction"
])

with tab1:
    data_overview.render(df)

with tab2:
    categorical_analysis.render(df)

with tab3:
    numerical_analysis.render(df)

with tab4:
    prediction.render(df)

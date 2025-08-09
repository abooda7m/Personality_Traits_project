import streamlit as st
import plotly.express as px

def render(df):
    st.subheader(" Categorical Analysis")

    cat_cols = "personality_type"

    fig = px.histogram(df, x=cat_cols, color="personality_type", barmode="group")
    st.plotly_chart(fig )
    
    

    st.subheader(" Personality Type Distribution")

    fig = px.pie(
        df,
        names='personality_type',
        title='Distribution of Personality Types',
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4
    )

    st.plotly_chart(fig, use_container_width=True)


    
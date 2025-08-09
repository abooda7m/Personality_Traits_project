import streamlit as st
import plotly.express as px

def render(df):
    st.subheader(" Numerical Analysis")

    num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()


    
    
    
    
    
    st.subheader("Social Energy by Personality Type")

    # Create a boxplot for social_energy split by personality type
    fig = px.box(
        df,
        x='personality_type',
        y='social_energy',
        color='personality_type',
        points='all'  # Show all data points to visualize distribution and outliers
    )

    # Customize layout
    fig.update_layout(
        xaxis_title='Personality Type',
        yaxis_title='Social Energy Score',
        showlegend=False
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    
    
    


    st.subheader(" Distribution of Emotional Stability")
    
    fig = px.histogram(
        df,
        x='emotional_stability',
        nbins=30,
        title='Distribution of Emotional Stability',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    fig.update_layout(
        xaxis_title='Emotional Stability',
        yaxis_title='Count',
        bargap=0.05,
        template='simple_white',
        title_font_size=20,
        font=dict(family='Arial', size=14)
    )
    
    fig.update_xaxes(showgrid=True, ticks="outside")
    fig.update_yaxes(showgrid=True, ticks="outside")
    
    st.plotly_chart(fig, use_container_width=True)
    

    st.subheader(" Average Value of Each Personality Trait")

    # Drop the target column
    numeric_features = df.drop(columns=['personality_type'])

    # Compute means
    mean_values = numeric_features.mean().sort_values(ascending=True).reset_index()
    mean_values.columns = ['Feature', 'Mean']

    # Plot bar chart
    fig = px.bar(
        mean_values,
        x='Mean',
        y='Feature',
        orientation='h',
        title='Average Value of Each Feature',
        text='Mean'
    )

    # Layout settings
    fig.update_layout(
        xaxis_title='Average Score',
        yaxis_title='Feature',
        height=800,
        width=900
    )

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

    # Show in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    
    



    st.subheader(" Alone Time vs. Party Liking")

    fig = px.scatter(
        df,
        x='alone_time_preference',
        y='party_liking',
        color='personality_type',
        title='Personality Types: Preference for Alone Time vs. Party Liking',
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        xaxis_title='Alone Time Preference',
        yaxis_title='Party Liking'
    )

    st.plotly_chart(fig, use_container_width=True)




    st.subheader("Travel Desire and Gadget Usage by Personality Type")

    # Group by personality_type and calculate the average of selected features
    avg_preferences = df.groupby('personality_type')[['travel_desire', 'gadget_usage']].mean().reset_index()

    # Create grouped bar chart
    fig = px.bar(
        avg_preferences,
        x='personality_type',
        y=['travel_desire', 'gadget_usage'],
        barmode='group',
        title='Average Travel Desire and Gadget Usage by Personality Type',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    # Customize layout
    fig.update_layout(
        xaxis_title='Personality Type',
        yaxis_title='Average Score'
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    

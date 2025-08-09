import streamlit as st

def render(df):
    st.subheader("Data Overview")

    # Dataset Summary
    st.markdown("""
    **Source:** Kaggle Dataset – Introvert, Extrovert & Ambivert Classification  
    **Records:** 20,000 entries (29 numeric features + 1 target label)  
    **Type:** Synthetic survey responses simulating personality profiles  
    **Missing Values:** None  
    **Outliers:** Removed using IQR method  
    **Label Balance:** Relatively balanced across classes
    """)

    st.markdown("---")

    # Data Quality Checks
    st.markdown("### Data Quality & Reliability")
    st.markdown("""
    - **Reliability:** Synthetic dataset, may lead to unrealistically high model performance. Controlled noise added for realism.  
    - **Consistency:** All features scaled 0–10, no mixed data types, clean labels and column names.  
    - **Relevance:** All features directly relate to personality classification.  
    - **Completeness:** 100% filled data, no missing values or dropped rows.
    """)

    st.markdown("---")

    # Timeliness
    st.markdown("### Timeliness")
    st.markdown("""
    - No time-based fields (timestamps/dates).  
    - Not time-sensitive; remains valid regardless of date.
    """)

    st.markdown("---")

    # Uniqueness
    st.markdown("### Uniqueness")
    st.markdown("""
    - Connects data science with real human traits (e.g., social energy, alone time preference, talkativeness).  
    - Uses before/after boxplots to show the effect of outlier removal.  
    - 3-class classification problem, not just binary.
    """)

    st.markdown("---")

    # Display sample data
    st.write("### Sample Data")
    st.dataframe(df.head())

    # Stats
    st.write("### Statistical Summary")
    st.write(df.describe())

    # Missing values
    st.write("### Missing Values")
    st.write(df.isnull().sum())

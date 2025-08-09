import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

def render(df):
    st.subheader("Personality Prediction (Simple Model)")

    # Define target and features
    target = 'personality_type'
    X = df.drop(columns=[target])
    y = df[target]

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Random Forest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    st.success("Model trained successfully!")

    # Predictions
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Display metrics
    st.markdown("### Model Performance on Test Set")
    st.write(f"**Accuracy:** {accuracy:.3f}")
    st.write(f"**Precision:** {precision:.3f}")
    st.write(f"**Recall:** {recall:.3f}")
    st.write(f"**F1-score:** {f1:.3f}")

    st.markdown("---")
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def render(df):
    st.subheader("Personality Prediction (Simple Model)")

    target = 'personality_type'
    X = df.drop(columns=[target])
    y = df[target]

    # Keep model in session state
    if "model" not in st.session_state:
        st.session_state.model = None

    # Train model button
    if st.button("Train Model"):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        st.session_state.model = model
        st.session_state.X_test = X_test
        st.session_state.y_test = y_test
        st.success("Model trained successfully!")

        # Evaluation
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')

        st.markdown("### Model Performance on Test Set")
        st.write(f"**Accuracy:** {accuracy:.3f}")
        st.write(f"**Precision:** {precision:.3f}")
        st.write(f"**Recall:** {recall:.3f}")
        st.write(f"**F1-score:** {f1:.3f}")

    st.markdown("---")

    # Prediction section
    if st.session_state.model is not None:
        st.write("### Try Prediction")
        input_data = []
        for col in X.columns:
            # Let user pick a number from 1 to 10
            value = st.selectbox(f"{col} (1-10)", list(range(1, 11)), index=4)
            input_data.append(value)

        if st.button("Predict Personality"):
            prediction = st.session_state.model.predict([input_data])[0]
            st.success(f"Predicted Personality: {prediction}")
    else:
        st.info("Please train the model first before making predictions.")

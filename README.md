# Personality Traits Classification Dashboard

## Overview
This project is an interactive Streamlit dashboard for analyzing and predicting personality types (Introvert, Extrovert, Ambivert) based on a synthetic dataset of 29 psychological and behavioral traits.  
It includes data exploration, visual analytics, and a simple machine learning prediction tool.

---

## Dataset
- Source: Kaggle – Introvert, Extrovert & Ambivert Classification  
- Records: 20,000 entries  
- Features: 29 numeric features (scaled 0–10) + 1 target label (`personality_type`)  
- Type: Synthetic survey-style responses simulating personality profiles  
- Label Balance: Relatively balanced across all classes  

### Example Features:
- `social_energy`
- `talkativeness`
- `empathy`
- `risk_taking`
- `planning`
- `travel_desire`
- and more...

---

## Project Structure
```
project/
│
├── main.py                       # Main app launcher
├── data/                         
│   └── load_data.py               # Load dataset from CSV
├── tabs/
│   ├── data_overview.py           # Dataset overview & quality checks
│   ├── categorical_analysis.py    # Analysis of categorical features
│   ├── numerical_analysis.py      # Analysis of numerical features & correlations
│   ├── prediction.py              # Personality type prediction tool
│
├── filters/
│   └── sidebar_filters.py         # Sidebar filtering options
│
├── personality_synthetic_dataset.csv  # Dataset file
└── README.md                      # Project documentation
```

---

## Features
1. Data Overview  
   - Displays dataset info, source, reliability, completeness, and sample preview.

2. Categorical Analysis  
   - Frequency counts and distributions of categorical features.

3. Numerical Analysis  
   - Boxplots, histograms, scatter plots, and feature averages.

4. Prediction  
   - Interactive model using Random Forest Classifier.
   - Users can input values for each feature (1–10) to predict personality type.
   - Displays evaluation metrics (Accuracy, Precision, Recall, F1-Score).

---

## Installation & Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personality-dashboard.git
   cd personality-dashboard
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate    # On macOS/Linux
   env\Scripts\activate       # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run main.py
   ```

---

## Requirements
Main libraries:
- `streamlit`
- `pandas`
- `plotly`
- `scikit-learn`

Install them with:
```bash
pip install streamlit pandas plotly scikit-learn
```

---

## License
This project is open-source and available under the MIT License.

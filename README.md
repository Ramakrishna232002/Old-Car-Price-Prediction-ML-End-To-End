# 🚗 Old Car Price Prediction ML Project

A full-stack Machine Learning project that predicts **used car prices** based on user inputs.  
It uses a **Python ML backend (FastAPI)** and a **React frontend** for dynamic, real-time price predictions.

---

## ✨ Features

- Dynamic React frontend for user input
- Real-time car price prediction using FastAPI
- Trained XGBoost regression model
- Encoders and preprocessing handled server-side
- Input validations and clean UI
- Modular, scalable project structure
- Easy to extend with new features or models

---

## 📁 Project Structure

```text
OLD CAR PRICE PREDICTION/
│
├── artifacts/                  # Generated artifacts & temporary files
│
├── backend/                    # FastAPI Backend
│   ├── __pycache__/
│   └── main.py                 # API endpoints & prediction logic
│
├── data/                       # Dataset storage
│   ├── raw/
│   │   └── used_cars.csv       # Raw dataset
│   └── processed/
│       └── cleaned_cars.pkl    # Cleaned & processed data
│
├── frontend/                   # React Frontend
│   ├── public/
│   └── src/
│       ├── api/
│       │   └── predictAPI.js   # Axios API calls
│       │
│       ├── components/
│       │   ├── CarForm.jsx     # Main UI form
│       │   └── CarForm.css     # Styling
│       │
│       ├── App.js              # Root component
│       ├── App.css             # Global styles
│       ├── index.js            # Entry point
│       ├── index.css
│       ├── reportWebVitals.js
│       └── setupTests.js
│
├── models/                     # Trained ML models
│   ├── xgb_model.pkl           # XGBoost model
│   ├── encoders.pkl            # Label encoders
│   ├── train_idx.pkl
│   └── test_idx.pkl
│
├── notebooks/                  # EDA & experiments
│   ├── 01_eda_and_cleaning.ipynb
│   └── src/
│       ├── components/
│       ├── pipelines/
│       ├── utils.py
│       ├── logger.py
│       └── exception.py
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🛠 Tech Stack
 
- **Backend**: Python, FastAPI, Pydantic
- **Frontend**: React, JavaScript, HTML, CSS
- **Machine Learning**: scikit-learn / pandas / numpy
- **Deployment / Dev**: Uvicorn, npm

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd OLD\ CAR\ PRICE\ PREDICTION
```

### 2. Backend Setup
```bash
# Navigate to backend folder
cd backend
 
# Install Python dependencies
pip install -r requirements.txt
 
# Run FastAPI server
PYTHONPATH=. uvicorn main:app --reload
```

### 3. Frontend Setup
```bash
# Navigate to frontend
cd frontend
 
# Install dependencies
npm install
 
# Start React development server
npm start
```
 
## � Usage
 
1. Open the frontend URL in your browser.
2. Fill the house details in the interactive form:
    - Fuel Type, Transmission, Horse Power (HP), Engine Displacement, 
    - Engine Type (V Engine / DOHC / Turbo / Other), Clean Title
    - Accident Impact, Vehicle Age, Mileage per Year
3. Click **Predict Price**.
4. Predicted Car price will appear dynamically below the form.
 
## 🧩 ML Pipeline
 
1. User inputs are collected from the React UI.
2. FastAPI backend:
    - Maps categorical values
    - Applies saved encoders
    - Loads trained XGBoost model
3. Model predicts price (log-scale → inverse transformed).
4. Prediction returned as JSON to frontend.
 
## 🎨 Frontend Details
 
- Built using React.
- Fully dynamic form – no hard-coded values.
- Dropdowns for categorical fields
- Validations for numeric inputs
- Form submission triggers fetch to FastAPI backend.
- Interactive UI for better user experience.
- Easily extendable for new input fields or styling.

## 👨‍💻 Author

- Ramakrishna Tagore
- Machine Learning|Data Scientist
 

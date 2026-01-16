from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
import os

# Initialize FastAPI
app = FastAPI(title="Old Car Price Prediction API")

# -------- Enable CORS --------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- Load Model and Encoders --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "../models")

with open(os.path.join(MODELS_DIR, "xgb_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(MODELS_DIR, "encoders.pkl"), "rb") as f:
    encoders = pickle.load(f)

# -------- Mappings for user-friendly input --------
FUEL_TYPE_MAP = {"Gasoline": 0, "Hybrid": 1, "Diesel": 2, "Other": 3}
TRANSMISSION_MAP = {"Manual": 0, "Automatic": 1, "Other": 2}

# -------- Pydantic Model --------
class CarInput(BaseModel):
    fuel_type: str
    transmission: str
    clean_title: int
    hp: float
    engine_displacement: float
    is_v_engine: int
    turbo: int
    dohc: int
    Accident_Impact: int
    Vehicle_Age: int
    Mileage_per_Year: float

# -------- Prediction Route --------
@app.post("/predict")
def predict_price(car: CarInput):
    try:
        # Convert JSON to DataFrame
        df = pd.DataFrame([car.dict()])

        # Rename columns to match training
        df.rename(columns={"engine_displacement": "engine displacement"}, inplace=True)

        # Map string categorical features to integers
        df["fuel_type"] = df["fuel_type"].map(FUEL_TYPE_MAP)
        df["transmission"] = df["transmission"].map(TRANSMISSION_MAP)

        # Encode other categorical columns
        for col in ["is_v_engine", "turbo", "dohc", "clean_title"]:
            if col in encoders:
                df[col] = encoders[col].transform(df[col])

        # Predict (log scale)
        predicted_log_price = model.predict(df)[0]

        # Inverse log-transform
        predicted_price = np.expm1(predicted_log_price)

        return {"predicted_price": round(float(predicted_price), 2)}

    except Exception as e:
        return {"error": str(e)}

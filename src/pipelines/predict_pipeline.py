# File: src/pipelines/predict_pipeline.py

import os
import pickle
import pandas as pd
import numpy as np

class PredictPipeline:
    def __init__(self):
        # Project root
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        # Load trained XGBoost model
        model_path = os.path.join(project_root, "models", "xgb_model.pkl")
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        # Load encoders
        encoders_path = os.path.join(project_root, "models", "encoders.pkl")
        with open(encoders_path, "rb") as f:
            self.encoders = pickle.load(f)

        # Columns
        self.categorical_columns = ['fuel_type', 'transmission', 'is_v_engine', 'turbo', 'dohc']

    def predict(self, input_dict):
        """
        input_dict must have all features, with integers for fuel_type and transmission.
        Example:
        {
            "fuel_type": 2, "transmission": 1, "clean_title": 1,
            "hp": 140, "engine displacement": 1.8, "is_v_engine": 0,
            "turbo": 0, "dohc": 1, "Accident_Impact": 0,
            "Vehicle_Age": 8, "Mileage_per_Year": 5600
        }
        """
        df = pd.DataFrame([input_dict])

        # Apply encoders (integer columns only)
        string_categorical = []  # currently none, as model trained on integers
        for col in string_categorical:
            df[col] = self.encoders[col].transform(df[col])

        # Predict log price
        predicted_log_price = self.model.predict(df)[0]

        # Convert back to original price
        predicted_price = np.expm1(predicted_log_price)
        return predicted_price

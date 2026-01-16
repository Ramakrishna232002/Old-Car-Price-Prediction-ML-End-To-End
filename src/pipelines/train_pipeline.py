import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor

def train_xgb_model():
    """
    Train an XGBoost Regressor on cleaned car data,
    apply log-transform on price, encode categorical features,
    and save the model and encoders.
    """
    # Base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load cleaned data
    data_path = os.path.join(base_dir, "../../data/processed/cleaned_cars.pkl")
    print(f"Loading cleaned data from: {data_path}")
    df = pd.read_pickle(data_path)

    # Features and target
    X = df.drop(columns=['price'])
    y = df['price']

    # Log-transform target
    y_log = np.log1p(y)

    # Encode categorical columns
    categorical_columns = ['fuel_type', 'transmission', 'is_v_engine', 'turbo', 'dohc']
    encoders = {}
    for col in categorical_columns:
        encoder = LabelEncoder()
        X[col] = encoder.fit_transform(X[col])
        encoders[col] = encoder

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_log, test_size=0.2, random_state=42
    )

    # Initialize XGBoost Regressor
    xgb = XGBRegressor(
        n_estimators=3000,
        max_depth=10,
        learning_rate=0.02,
        subsample=0.9,
        colsample_bytree=0.9,
        min_child_weight=5,
        gamma=0.1,
        reg_alpha=0.2,
        reg_lambda=2.0,
        objective='reg:squarederror',
        random_state=42,
        n_jobs=-1
    )

    # Train model
    xgb.fit(X_train, y_train)
    print("XGBoost training complete!")

    # Create models folder if not exists
    models_dir = os.path.join(base_dir, "../../models")
    os.makedirs(models_dir, exist_ok=True)

    # Save trained model
    model_path = os.path.join(models_dir, "xgb_model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(xgb, f)

    # Save encoders
    encoders_path = os.path.join(models_dir, "encoders.pkl")
    with open(encoders_path, "wb") as f:
        pickle.dump(encoders, f)

    print(f"XGBRegressor saved at: {os.path.abspath(model_path)}")
    print(f"Encoders saved at: {os.path.abspath(encoders_path)}")

if __name__ == "__main__":
    train_xgb_model()

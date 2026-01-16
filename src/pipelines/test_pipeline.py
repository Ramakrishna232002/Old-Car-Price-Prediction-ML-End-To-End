import os
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def test_xgb_model():
    """
    Load the trained XGBoost model and encoders,
    apply preprocessing to features, inverse log-transform the predictions,
    and evaluate on the test set.
    """
    # Project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    # Paths
    model_path = os.path.join(project_root, "models", "xgb_model.pkl")
    encoders_path = os.path.join(project_root, "models", "encoders.pkl")
    data_path = os.path.join(project_root, "data", "processed", "cleaned_cars.pkl")

    # Load data
    df = pd.read_pickle(data_path)
    X = df.drop(columns=['price'])
    y = df['price']

    # Load encoders
    with open(encoders_path, "rb") as f:
        encoders = pickle.load(f)

    # Apply label encoding
    categorical_columns = ['fuel_type', 'transmission', 'is_v_engine', 'turbo', 'dohc']
    for col in categorical_columns:
        X[col] = encoders[col].transform(X[col])

    # Load trained XGBoost model
    with open(model_path, "rb") as f:
        xgb = pickle.load(f)

    # Train-test split (same split as training)
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Predict in log scale
    y_pred_log = xgb.predict(X_test)

    # Inverse log-transform to original price scale
    y_pred = np.expm1(y_pred_log)

    # Metrics
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print("XGBoost Model Evaluation on Test Set")
    print("------------------------------------")
    print(f"MAE : {mae}")
    print(f"RMSE: {rmse}")
    print(f"R2  : {r2}")

if __name__ == "__main__":
    test_xgb_model()

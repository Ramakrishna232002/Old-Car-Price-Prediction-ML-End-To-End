# File: src/pipelines/test_predict_pipeline.py

from src.pipelines.predict_pipeline import PredictPipeline

if __name__ == "__main__":
    predictor = PredictPipeline()

    # Sample input (integers for fuel_type and transmission!)
    sample_car = {
        "fuel_type": 2,          # Petrol=2, Diesel=0, Hybrid=1 (example mapping)
        "transmission": 1,       # Manual=1, Automatic=0
        "clean_title": 1,
        "hp": 140,
        "engine displacement": 1.8,
        "is_v_engine": 0,
        "turbo": 0,
        "dohc": 1,
        "Accident_Impact": 0,
        "Vehicle_Age": 8,
        "Mileage_per_Year": 5600
    }

    price = predictor.predict(sample_car)
    print(f"\nPredicted Car Price: ₹ {round(price, 2)}")

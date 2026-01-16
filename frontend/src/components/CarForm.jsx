import React, { useState } from "react";
import { FaCarSide, FaMoneyBillWave, FaCog } from "react-icons/fa";
import { predictCarPrice } from "../api/predictAPI";
import "./CarForm.css";

const CarForm = () => {
  const [formData, setFormData] = useState({
    fuel_type: "",
    transmission: "",
    clean_title: "",
    hp: "",
    engine_displacement: "",
    is_v_engine: 0,
    turbo: 0,
    dohc: 0,
    other_engine: 0,
    Accident_Impact: 0,
    Vehicle_Age: "",
    Mileage_per_Year: "",
  });

  const [predictedPrice, setPredictedPrice] = useState(null);

  const fuelOptions = ["Gasoline", "Hybrid", "Diesel", "Other"];
  const transmissionOptions = ["Manual", "Automatic", "Other"];
  const cleanTitleOptions = ["Yes", "No"];

  const handleChange = (e) => {
    const { name, value, checked } = e.target;

    if (name === "engine_displacement") {
      const val = parseFloat(value);
      if (val > 10 || val < 1) {
        alert("Please enter value between 1-10");
        return;
      }
    }

    if (["is_v_engine", "turbo", "dohc", "other_engine"].includes(name)) {
      setFormData((prev) => ({
        ...prev,
        is_v_engine: name === "is_v_engine" ? checked ? 1 : 0 : prev.is_v_engine,
        turbo: name === "turbo" ? checked ? 1 : 0 : prev.turbo,
        dohc: name === "dohc" ? checked ? 1 : 0 : prev.dohc,
        other_engine: name === "other_engine" ? checked ? 1 : 0 : prev.other_engine,
      }));
      return;
    }

    if (name === "Accident_Impact") {
      setFormData((prev) => ({ ...prev, Accident_Impact: parseInt(value) }));
      return;
    }

    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        ...formData,
        clean_title: formData.clean_title === "Yes" ? 1 : 0,
      };
      const res = await predictCarPrice(payload);
      setPredictedPrice(res.predicted_price);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="form-container">
      <div className="form-header">
        <FaCarSide className="header-icon" />
        <h1>Old Car Price Prediction</h1>
      </div>

      <form onSubmit={handleSubmit} className="car-form">
        <div className="form-row">
          <label>Fuel Type</label>
          <select name="fuel_type" value={formData.fuel_type} onChange={handleChange} required>
            <option value="">Select Fuel</option>
            {fuelOptions.map((f) => (
              <option key={f} value={f}>{f}</option>
            ))}
          </select>
        </div>

        <div className="form-row">
          <label>Transmission</label>
          <select name="transmission" value={formData.transmission} onChange={handleChange} required>
            <option value="">Select Transmission</option>
            {transmissionOptions.map((t) => (
              <option key={t} value={t}>{t}</option>
            ))}
          </select>
        </div>

        <div className="form-row">
          <label>Clean Title</label>
          <select name="clean_title" value={formData.clean_title} onChange={handleChange} required>
            <option value="">Select Option</option>
            {cleanTitleOptions.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </div>

        <div className="form-row">
          <label>Horsepower (Hp)</label>
          <input
            type="number"
            placeholder="Please enter Hp value"
            name="hp"
            value={formData.hp}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-row">
          <label>Engine Displacement (1-10)</label>
          <input
            type="number"
            step="0.1"
            placeholder="Enter value 1-10"
            name="engine_displacement"
            value={formData.engine_displacement}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-row">
          <label>Engine Type <FaCog /></label>
          <div className="checkbox-group">
            <label><input type="checkbox" name="is_v_engine" checked={formData.is_v_engine} onChange={handleChange} /> V Engine</label>
            <label><input type="checkbox" name="dohc" checked={formData.dohc} onChange={handleChange} /> DOHC</label>
            <label><input type="checkbox" name="turbo" checked={formData.turbo} onChange={handleChange} /> Turbo</label>
            <label><input type="checkbox" name="other_engine" checked={formData.other_engine} onChange={handleChange} /> Other</label>
          </div>
        </div>

        <div className="form-row">
          <label>Accident Impact</label>
          <div className="checkbox-group">
            <label><input type="radio" name="Accident_Impact" value={1} checked={formData.Accident_Impact === 1} onChange={handleChange} /> At least 1</label>
            <label><input type="radio" name="Accident_Impact" value={0} checked={formData.Accident_Impact === 0} onChange={handleChange} /> None</label>
          </div>
        </div>

        <div className="form-row">
          <label>Vehicle Age</label>
          <input type="number" name="Vehicle_Age" value={formData.Vehicle_Age} onChange={handleChange} required />
        </div>

        <div className="form-row">
          <label>Mileage per Year</label>
          <input type="number" name="Mileage_per_Year" value={formData.Mileage_per_Year} onChange={handleChange} required />
        </div>

        <button type="submit" className="submit-btn">Predict Price</button>
      </form>

      {predictedPrice && (
        <div className="predicted-price">
          <FaMoneyBillWave className="money-icon" />
          Predicted Price: ₹ {predictedPrice}
        </div>
      )}
    </div>
  );
};

export default CarForm;

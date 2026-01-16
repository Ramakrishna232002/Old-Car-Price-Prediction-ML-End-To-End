import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const predictCarPrice = async (carData) => {
  try {
    const response = await axios.post(`${BASE_URL}/predict`, carData);
    return response.data;
  } catch (error) {
    console.error("Axios Error:", error);
    return { error: error.message };
  }
};

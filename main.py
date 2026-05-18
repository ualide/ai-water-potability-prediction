from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# حل مشكل الاتصال
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل الملفات
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

print("✅ API: Model and Scaler are Ready!")

class WaterData(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

@app.post("/predict")
def predict(data: WaterData):
    try:
        features = np.array([[
            data.ph, data.Hardness, data.Solids, data.Chloramines,
            data.Sulfate, data.Conductivity, data.Organic_carbon,
            data.Trihalomethanes, data.Turbidity
        ]])
        
        # التوقع Prediction
        scaled = scaler.transform(features)
        pred = int(model.predict(scaled)[0])
        
        # حساب نسبة اليقين Confidence
        probs = model.predict_proba(scaled)[0]
        confidence = float(max(probs))

        return {
            "prediction": pred,
            "label": "Drinkable" if pred == 1 else "Not Drinkable",
            "confidence": confidence
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI
from app.models.request_model import FlightData
from app.services.predict import predict_delay

app = FastAPI(title="Flight Delay Prediction API")

@app.get("/")
def home():
    return {"message": "Welcome to Flight Delay Prediction API"}

@app.post("/predict")
def predict(data: FlightData):
    result = predict_delay(data)
    return {"predicted_arrival_delay": result}

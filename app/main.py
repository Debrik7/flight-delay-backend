from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.request_model import FlightInput
from app.services.predict import predict_regression, predict_classification

app = FastAPI(title="Flight Delay Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Flight Delay Prediction API"}

@app.post("/predict/regression")
def predict_reg(data: FlightInput):
    try:
        predicted_delay = predict_regression(data.dict())
        return {"predicted_delay_minutes": predicted_delay}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predict/classification")
def predict_clf(data: FlightInput):
    try:
        try:
            payload = data.model_dump()   # v2
        except AttributeError:
            payload = data.dict()         # v1

        delay_probability = predict_classification(payload)
        return {"delay_probability": delay_probability}
    except Exception as e:
        return {"error": str(e)}

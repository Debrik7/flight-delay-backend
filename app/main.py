from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.request_model import FlightData
from app.services.predict import predict_delay

app = FastAPI(title="Flight Delay Prediction API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Flight Delay Prediction API"}

@app.post("/predict")
def predict(data: FlightData):
    result = predict_delay(data)
    return {"predicted_arrival_delay": result}

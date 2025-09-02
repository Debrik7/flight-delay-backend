import numpy as np
from app.utils.load_model import load_model

model = load_model()

def predict_delay(data):
    features = np.array([
        data.DEPARTURE_DELAY,
        data.TAXI_OUT,
        data.TAXI_IN,
        data.AIR_TIME,
        data.ELAPSED_TIME,
        data.SCHEDULED_TIME,
        data.WEATHER_DELAY,
        data.ORIGIN_AIRPORT,
        data.DESTINATION_AIRPORT,
        data.AIRLINE
    ]).reshape(1, -1)

    prediction = model.predict(features)
    return round(float(prediction[0]), 2)

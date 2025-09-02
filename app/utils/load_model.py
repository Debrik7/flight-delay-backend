import pickle

def load_model():
    with open("xgb_weather_only_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

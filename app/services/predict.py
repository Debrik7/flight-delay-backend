import pandas as pd
import xgboost as xgb
from app.utils.load_model import load_models_and_encoders
from app.services.feature_engineering import add_features

models = load_models_and_encoders()
reg_model = models["regression"]["model"]
reg_features = models["regression"]["features"]
clf_model = models["classification"]["model"]
clf_features = models["classification"]["features"]
clf_threshold = models["classification"]["threshold"]
encoders = models["encoders"]

def encode_input(df: pd.DataFrame) -> pd.DataFrame:
    for col, enc in encoders.items():
        if col in df.columns:
            df[col] = enc.transform(df[col].astype(str))
    return df

def predict_regression(data_dict: dict) -> float:
    df = pd.DataFrame([data_dict])
    df = encode_input(df)
    df = add_features(df)
    X = df[reg_features]
    pred = reg_model.predict(X)[0]
    return round(float(pred), 2)

def predict_classification(data_dict: dict) -> float:
    df = pd.DataFrame([data_dict])
    df = encode_input(df)
    df = add_features(df)
    X = df[clf_features]

    dtest = xgb.DMatrix(X, feature_names=clf_features)
    y_proba = float(clf_model.predict(dtest)[0])  
    return round(y_proba, 4)

import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
MODEL_DIR = os.path.join(BASE_DIR, "models") 

def load_models_and_encoders():
    reg_bundle = joblib.load(os.path.join(MODEL_DIR, "regressor_models.pkl"))
    reg_model = reg_bundle["LightGBM"]
    reg_features = reg_bundle["features"]

    clf_bundle = joblib.load(os.path.join(MODEL_DIR, "xgboost_new_smote_model.pkl"))
    clf_model = clf_bundle["booster"]
    clf_features = clf_bundle["feature_cols"]
    clf_threshold = clf_bundle["threshold"]

    label_cols = ['AIRLINE', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'ORIGIN_WEATHER']
    encoders = {}
    for col in label_cols:
        enc_path = os.path.join(MODEL_DIR, f"{col}_encoder.pkl")
        encoders[col] = joblib.load(enc_path)

    return {
        "regression": {"model": reg_model, "features": reg_features},
        "classification": {"model": clf_model, "features": clf_features, "threshold": clf_threshold},
        "encoders": encoders
    }

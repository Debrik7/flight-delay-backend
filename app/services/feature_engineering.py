import numpy as np
import pandas as pd

def parse_hhmm_to_minutes(x):
    try:
        xi = int(x) % 2400
        hh, mm = xi // 100, xi % 100
        return xi if mm >= 60 else hh * 60 + mm
    except:
        return np.nan

def add_features(df):
    df['sched_min_of_day'] = df['SCHEDULED_DEPARTURE'].apply(parse_hhmm_to_minutes)
    df['sched_hour'] = (df['sched_min_of_day'] // 60).fillna(0).astype(int)
    df['sched_minute'] = (df['sched_min_of_day'] % 60).fillna(0).astype(int)
    df['sched_sin'] = np.sin(2 * np.pi * df['sched_min_of_day'] / 1440)
    df['sched_cos'] = np.cos(2 * np.pi * df['sched_min_of_day'] / 1440)
    df['origin_wind_q'] = pd.qcut(df['ORIGIN_WIND_SPEED'].fillna(0), q=4, labels=False, duplicates='drop')
    df['wind_high'] = (df['origin_wind_q'] == df['origin_wind_q'].max()).astype(int)
    df['route_prod'] = df['ORIGIN_AIRPORT'].astype(int) * df['DESTINATION_AIRPORT'].astype(int)
    df['route_diff'] = (df['DESTINATION_AIRPORT'].astype(int) - df['ORIGIN_AIRPORT'].astype(int)).abs()
    df['airline_month'] = df['AIRLINE'].astype(int) * df['MONTH'].astype(int)
    return df

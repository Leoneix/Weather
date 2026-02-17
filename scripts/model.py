import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

df = pd.read_csv("data/processed/weather_features.csv")

features = [
    "lat","lon",
    "hour_sin","hour_cos","day_sin","day_cos",
    "relativehumidity_2m","pressure_msl","windspeed_10m","precipitation",
    "temp_lag_1","temp_lag_3","temp_lag_6","temp_lag_12","temp_lag_24"
]

X =df[features]
y = df["target_temp_24h"]

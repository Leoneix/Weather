import pandas as pd
import numpy as np
import glob
import os

files = glob.glob("data/raw/*.csv")
df = pd.concat([pd.read_csv(f) for f in files])

df["time"] = pd.to_datetime(df["time"])

df["hour"] = df["time"].dt.hour
df["day"] = df["time"].dt.dayofyear

df["hour_sin"] = np.sin(2*np.pi*df["hour"]/24)
df["hour_cos"] = np.cos(2*np.pi*df["hour"]/24)
df["day_sin"] = np.sin(2*np.pi*df["day"]/365)
df["day_cos"] = np.cos(2*np.pi*df["day"]/365)

df = df.sort_values(["city","time"])

for lag in [1,3,6,12,24]:
    df[f"temp_lag_{lag}"] = df.groupby("city")["temperature_2m"].shift(lag)

df["target_temp_24h"] = df.groupby("city")["temperature_2m"].shift(-24)

df = df.dropna()
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/weather_features.csv", index=False)
print("Feature file created")
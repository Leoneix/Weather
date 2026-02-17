import requests
import pandas as pd
import os

cities = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "bengaluru": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867),
    "jaipur": (26.9124, 75.7873),
    "lucknow": (26.8467, 80.9462),
}

START = "2023-01-01"
END = "2024-01-01"

os.makedirs("data/raw", exist_ok=True)

for city, (lat, lon) in cities.items():
    print("Downloading:", city)

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}"
        f"&start_date={START}&end_date={END}"
        f"&hourly=temperature_2m,relativehumidity_2m,pressure_msl,windspeed_10m,precipitation"
    )

    r = requests.get(url).json()

    df = pd.DataFrame(r["hourly"])
    df["city"] = city
    df["lat"] = lat
    df["lon"] = lon

    df.to_csv(f"data/raw/{city}.csv", index=False)

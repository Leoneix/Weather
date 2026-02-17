import pandas as pd
import numpy as np
import glob

files = glob.glob("data/raw/*.csv")
df = pd.concat([pd.read_csv(f) for f in files])

df["time"] = pd.to_datetime
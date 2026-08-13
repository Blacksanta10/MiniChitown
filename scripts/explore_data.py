# Used to explore the raw CTA data

import pandas as pd

stops = pd.read_csv("data/raw/stops.txt")

print(stops[["stop_id", "stop_code", "stop_name", "stop_lat", "stop_lon"]].head(20))
print(stops.columns)
print(stops.shape)


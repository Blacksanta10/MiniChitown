import pandas as pd

def get_stops():
    """
    Reads the stops.txt file and returns a DataFrame with selected columns.
    """
    return pd.read_csv("data/raw/stops.txt")

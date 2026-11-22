import pandas as pd

def extract_data():
    df = pd.read_csv("data/sales.csv")

    return df
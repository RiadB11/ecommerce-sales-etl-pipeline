import pandas as pd

def transform_data(df):

    df = df.dropna()


    df = df.drop_duplicates()


    numeric_columns = [
        "quantity",
        "unit_price",
        "discount",
        "sales",
        "cost",
        "profit"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column])


    df = df[
        (df["unit_price"] > 0) &
        (df["quantity"] > 0)
    ]


    df["total_order_value"] = df["sales"]


    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    return df

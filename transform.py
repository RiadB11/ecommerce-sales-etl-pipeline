import pandas as pd

def transform_data(df):
    # Trajtojmë vlerat që mungojnë
    df = df.dropna()

    # Largohet rreshtat e duplikuar
    df = df.drop_duplicates()

    # Sigurohemi që kolonat numerike kanë tipe numerike
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

    # Kontrollojmë çmimet dhe sasitë
    df = df[
        (df["unit_price"] > 0) &
        (df["quantity"] > 0)
    ]

    # Krijojmë kolonën e vlerës totale të shitjes
    df["total_order_value"] = df["sales"]

    # Konvertojmë datat
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    return df

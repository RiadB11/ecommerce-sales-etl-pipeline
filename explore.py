from extract import extract_data

def explore_data(df):
    # Numri total i porosive
    print("Total Orders:", df["order_id"].nunique())

    # Numri i klientëve
    print("Total Customers:", df["customer_id"].nunique())

    # Numri i produkteve
    print("Total Products:", df["product_name"].nunique())

    # Kategoritë e produkteve
    print("Product Categories:")
    print(df["category"].unique())

    # Vlerat që mungojnë
    print("Missing Values:")
    print(df.isnull().sum())

    # Rreshtat e duplikuar
    print("Duplicate Rows:", df.duplicated().sum())

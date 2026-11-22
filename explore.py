from extract import extract_data

def explore_data(df):

    print("Total Orders:", df["order_id"].nunique())


    print("Total Customers:", df["customer_id"].nunique())


    print("Total Products:", df["product_name"].nunique())


    print("Product Categories:")
    print(df["category"].unique())


    print("Missing Values:")
    print(df.isnull().sum())


    print("Duplicate Rows:", df.duplicated().sum())

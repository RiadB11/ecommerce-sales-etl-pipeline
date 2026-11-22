from extract import extract_data
from explore import explore_data
from transform import transform_data
from database import get_database_connection
from load import load_data


df = extract_data()


explore_data(df)


df = transform_data(df)

print("\nTransformed Data:")
print(df.head())
print("\nNew Shape:", df.shape)


engine = get_database_connection()


with engine.connect() as connection:
    result = connection.exec_driver_sql(
        "SELECT current_database(), current_user, version()"
    )
    print("\nDatabase Information:")
    print(result.fetchone())


load_data(df, engine)


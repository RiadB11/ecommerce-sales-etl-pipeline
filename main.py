from extract import extract_data
from explore import explore_data
from transform import transform_data
from database import get_database_connection
from load import load_data

# 1. Data Extraction
df = extract_data()

# 2. Data Exploration
explore_data(df)

# 3. Data Transformation
df = transform_data(df)

print("\nTransformed Data:")
print(df.head())
print("\nNew Shape:", df.shape)

# 4. Database Connection
engine = get_database_connection()

# Check PostgreSQL connection
with engine.connect() as connection:
    result = connection.exec_driver_sql(
        "SELECT current_database(), current_user, version()"
    )
    print("\nDatabase Information:")
    print(result.fetchone())

# 5. Database Loading
load_data(df, engine)


def load_data(df, engine):

    df.to_sql(
        name="sales",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data successfully loaded into PostgreSQL!")
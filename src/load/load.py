def load_dataframe_to_db(df, conn):
    # Save DataFrame to the database using the provided connection.
    df.to_sql(
        'go_capstone_data',
        con=conn,
        schema='de_2506_a',
        if_exists='replace',
        index=False
    )
    print("Data loaded successfully to the database.")
    # Save additional local copy to /data/load
    df.to_csv('data/load/go_capstone_data.csv', index=False)

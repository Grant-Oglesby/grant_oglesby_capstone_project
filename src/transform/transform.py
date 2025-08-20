from src.transform.clean_co2 import clean_co2
from src.transform.clean_energy import clean_energy
import pandas as pd


# Columns to retain after transformation
# This function is used to ensure that only the necessary columns are kept
# in the final DataFrame
def retain_columns(df):
    df = df[
        [
            "country", "year", "iso_code", "population", "gdp", "co2",
            "co2_per_capita", "cumulative_co2", "cumulative_oil_co2",
            "oil_co2", "oil_co2_per_capita", "region",
            "coal_cons_per_capita", "coal_consumption", "energy_per_capita"
        ]
    ]
    return df


# Main transformation function that passes DataFrames through
# cleaning functions
def transform_data(df_co2, df_energy):
    # Cleans the data from the CO2 DataFrame
    df_co2_cleaned = clean_co2(df_co2)
    # Cleans the data from the Energy DataFrame
    df_energy_cleaned = clean_energy(df_energy)
    # Combine the cleaned DataFrames on the columns "country" and "year"
    df_combined = pd.merge(
        df_co2_cleaned,
        df_energy_cleaned,
        on=["country", "year"],
        how="inner"
    )
    # Retain only the necessary columns
    try:
        df_combined = retain_columns(df_combined)
    except Exception as e:
        print(f"Error retaining columns: {e}")
    # Save a copy of the transformed DataFrame
    # and return for loading to database
    df_combined.to_csv("data/transform/transformed_data.csv")
    return df_combined.reset_index(drop=True)

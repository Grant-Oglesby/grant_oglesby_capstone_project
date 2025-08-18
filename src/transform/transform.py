from src.transform.clean_co2 import clean_co2
from src.transform.clean_energy import clean_energy
import pandas as pd


def retain_columns(df):
    df = df[
        [
            'country', 'year', 'iso_code', 'population', 'gdp', 'co2',
            'co2_per_capita', 'cumulative_co2', 'cumulative_oil_co2',
            'oil_co2', 'oil_co2_per_capita', 'region',
            'coal_cons_per_capita', 'coal_consumption', 'energy_per_capita'
        ]
    ]
    return df


def transform_data(df_co2, df_energy):
    df_co2_cleaned = clean_co2(df_co2)
    df_energy_cleaned = clean_energy(df_energy)
    df_combined = pd.merge(
        df_co2_cleaned,
        df_energy_cleaned,
        on=['country', 'year'],
        how='inner'
    )
    try:
        df_combined = retain_columns(df_combined)
    except Exception as e:
        print(f"Error retaining columns: {e}")
    df_combined.to_csv('data/transform/transformed_data.csv')
    return df_combined.reset_index(drop=True)

from src.transform.clean_co2 import clean_co2
from src.transform.clean_energy import clean_energy
import pandas as pd


def transform_data(df_co2, df_energy):
    df_co2_cleaned = clean_co2(df_co2)
    df_energy_cleaned = clean_energy(df_energy)
    df_combined = pd.merge(
        df_co2_cleaned,
        df_energy_cleaned,
        on=['country', 'year'],
        how='inner'
    )
    return df_combined.reset_index(drop=True)

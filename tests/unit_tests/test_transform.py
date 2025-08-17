from src.transform.transform import transform_data
import pandas as pd


def test_transform_data():
    df_co2 = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'iso_code': [None, 'DZ', 'MX'],
        'country': ['Afghanistan', 'Algeria', 'Algeria'],
        'year': [1990, 2021, 2022],
        'gdp': [1000, 1200, 1500],
        'population': [10000, 20000, 30000]
    })
    df_energy = pd.DataFrame({
        'country': ['Afghanistan', 'Algeria', 'Algeria'],
        'iso_code': [None, 'DZ', 'DZ'],
        'year': [1990, 2021, 2022],
        'energy_consumption': [100, 200, 300],
        'gdp': [1000, 1200, 1500],
        'population': [10000, 20000, 30000],
        'energy_cons_change_pct': [0.1, 0.2, 0.3]
    })
    result = transform_data(df_co2, df_energy)
    assert result.shape[0] == 2
    assert 'country' in result.columns
    assert len(df_co2.columns) < len(result.columns)
    assert isinstance(result, pd.DataFrame)

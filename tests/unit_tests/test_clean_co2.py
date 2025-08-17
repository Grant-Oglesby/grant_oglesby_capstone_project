from src.transform.clean_co2 import (
    clean_co2,
    drop_unnecessary_columns,
    drop_records_outside_timeline,
    drop_records_with_missing_values,
    calculate_missing_values,
    drop_null_columns,
    convert_columns_types,
    enrich_data
)
import pandas as pd


# Function to test unnecessary column dropping
def test_drop_unnecessary_columns():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'country': ['A', 'B', 'C'],
        'year': [1990, 2021, 2022]
    })
    result = drop_unnecessary_columns(df)
    assert 'Unnamed: 0' not in result.columns
    assert 'country' in result.columns
    assert 'year' in result.columns


# Test records not between 1994 and 2023 are dropped
def test_drop_records_outside_timeline():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'country': ['A', 'B', 'C'],
        'year': [1990, 2021, 2022]
    })
    result = drop_records_outside_timeline(df)
    assert result.shape[0] == 2
    assert 'year' in result.columns


# Test records with missing values that cannot be calculated are dropped
def test_drop_records_with_missing_values():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'iso_code': [None, 'DZ', 'MX'],
        'country': ['Antarctica', 'Belgium', 'Algeria'],
        'year': [1994, 2021, 2022],
        'gdp': [1000, 1200, 1500]
    })
    result = drop_records_with_missing_values(df)
    assert result.shape[0] == 2
    assert 'year' in result.columns


# Test missing values are calculated for gdp column
# Grouped by country
def test_calculate_missing_values():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'country': ['A', 'B', 'B'],
        'year': [1994, 2021, 2022],
        'gdp': [1000, None, 1500]
    })
    result = calculate_missing_values(df)
    assert result.shape[0] == 3
    assert 'year' in result.columns
    assert 'gdp' in result.columns
    assert None not in result['gdp'].values


def test_drop_null_columns():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'country': ['A', 'B', 'C'],
        'year': [1990, 2021, 2022],
        'gdp': [1000, 0, 1500]
    })
    result = drop_null_columns(df)
    assert result.shape[1] == 3
    assert 'gdp' not in result.columns


def test_convert_columns_types():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'country': ['A', 'B', 'C'],
        'year': [1990, 2021, 2022],
        'gdp': [1000, 1200, 1500],
        'population': [10000, 20000, 30000]
    })
    result = pd.DataFrame(convert_columns_types(df))
    assert pd.api.types.is_integer_dtype(result['year'])
    assert pd.api.types.is_integer_dtype(result['gdp'])


def test_enrich_data():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'iso_code': [None, 'DZ', 'MX'],
        'country': ['Afghanistan', 'Algeria', 'Mexico'],
        'year': [1990, 2021, 2022],
        'gdp': [1000, 1200, 1500],
        'population': [10000, 20000, 30000]
    })
    result = enrich_data(df)
    assert 'region' in result.columns


def test_clean_co2():
    df = pd.DataFrame({
        'Unnamed: 0': [1, 2, 3],
        'iso_code': [None, 'DZ', 'MX'],
        'country': ['Afghanistan', 'Algeria', 'Algeria'],
        'year': [1990, 2021, 2022],
        'gdp': [1000, 1200, 1500],
        'population': [10000, 20000, 30000]
    })
    result = clean_co2(df)
    assert result.shape[0] == 2

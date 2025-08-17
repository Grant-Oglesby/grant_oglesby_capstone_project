from src.transform.clean_energy import (
    clean_energy,
    drop_unnecessary_columns,
    drop_records_outside_timeline,
    drop_columns_with_high_missing_values,
    fill_remaining_nulls
)
import pandas as pd


# Drop unnecessary columns
def test_drop_unnecessary_columns():
    data = {
        'Unnamed: 0': [1, 2, 3],
        'country': ['USA', 'Canada', 'Mexico'],
        'iso_code': ['USA', 'USA', 'USA'],
        'population': [331002651, 331002651, 331002651],
        'gdp': [21137518, 21137518, 21137518],
        'energy_cons_change_pct': [1.2, 1.2, 1.2]
    }
    df = pd.DataFrame(data)
    df_cleaned = drop_unnecessary_columns(df)
    assert 'Unnamed: 0' not in df_cleaned.columns
    assert 'iso_code' not in df_cleaned.columns
    assert 'population' not in df_cleaned.columns
    assert 'gdp' not in df_cleaned.columns
    assert 'energy_cons_change_pct' not in df_cleaned.columns


# Drop records outside 1994 and 2023
def test_drop_records_outside_timeline():
    data = {
        'year': [1990, 1995, 2000, 2025],
        'country': ['USA', 'Canada', 'Mexico', 'USA'],
        'iso_code': ['USA', 'CAN', 'MEX', 'USA'],
        'population': [331002651, 37742154, 128932753, 331002651],
        'gdp': [21137518, 21137518, 21137518, 21137518],
        'energy_cons_change_pct': [1.2, 1.2, 1.2, 1.2]
    }
    df = pd.DataFrame(data)
    df_cleaned = drop_records_outside_timeline(df)
    assert df_cleaned['year'].min() >= 1994
    assert df_cleaned['year'].max() <= 2023
    assert df_cleaned.shape[0] == 2


# Drop columns with high missing values
def test_drop_columns_with_high_missing_values():
    data = {
        'year': [1995, 2000, 2005, 2010],
        'country': ['USA', 'Canada', 'Mexico', 'USA'],
        'population': [331002651, 37742154, 128932753, 331002651],
        'gdp': [0, 21137518, 0, 21137518],
        'energy_cons_change_pct': [1.2, 1.2, 1.2, 1.2]
    }
    df = pd.DataFrame(data)
    df_cleaned = drop_columns_with_high_missing_values(df)
    assert 'gdp' not in df_cleaned.columns


# Fill remaining nulls, calculated by country
def test_fill_remaining_nulls():
    data = {
        'year': [1995, 2000, 2005, 2010],
        'country': ['USA', 'USA', 'Mexico', 'USA'],
        'population': [331002651, 37742154, 128932753, 331002651],
        'gdp': [0, 21137518, 21137518, 21137518],
        'energy_cons_change_pct': [1.2, 1.2, 1.2, 1.2]
    }
    df = pd.DataFrame(data)
    df_cleaned = fill_remaining_nulls(df)
    assert df_cleaned['gdp'].isnull().sum() == 0


# Test full energy cleaning process
def test_clean_energy():
    data = {
        'year': [1995, 2000, 2005, 2010],
        'country': ['USA', 'Canada', 'Mexico', 'USA'],
        'iso_code': [None, 'CAN', None, 'USA'],
        'population': [331002651, 37742154, 128932753, 331002651],
        'gdp': [21137518, 21137518, 21137518, 21137518],
        'energy_cons_change_pct': [1.2, 1.2, 1.2, 1.2],
        'energy_per_capita': [484.347, 386.491, 300.123, 341.219]
    }
    df = pd.DataFrame(data)
    df_cleaned = clean_energy(df)
    assert df_cleaned.shape[0] == 4

import pandas as pd


# Drop unnecessary columns
def drop_unnecessary_columns(df_energy):
    df_energy.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
    df_energy = df_energy.drop(
        columns=['iso_code', 'population', 'gdp', 'energy_cons_change_pct']
    )
    return df_energy


# Drop records outside the desired timeline
def drop_records_outside_timeline(df_energy):
    df_energy = df_energy[
        df_energy['year'].between(1994, 2023)
    ].reset_index(drop=True)
    return df_energy


# Drop columns with more than 5% missing values
def drop_columns_with_high_missing_values(df_energy):
    def count_zeros(df):
        return (df == 0).mean() * 100
    nulls_energy = pd.Series(count_zeros(df_energy))
    columns_to_keep = nulls_energy[nulls_energy <= 5].index.tolist()
    df_energy = df_energy[columns_to_keep]
    return df_energy


# Fill values of 0 with the mean of the rest of that column,
# for numeric columns only
def fill_remaining_nulls(df_energy):
    numeric_cols = df_energy.select_dtypes(include='number').columns
    for col in numeric_cols:
        df_energy[col] = df_energy.groupby('country')[col].transform(
            lambda x: x.mask(x == 0, x[x != 0].mean())
        )
    return df_energy


def clean_energy(df_energy):
    df_energy = drop_unnecessary_columns(df_energy)
    df_energy = drop_records_outside_timeline(df_energy)
    df_energy = drop_columns_with_high_missing_values(df_energy)
    df_energy = fill_remaining_nulls(df_energy)
    return df_energy

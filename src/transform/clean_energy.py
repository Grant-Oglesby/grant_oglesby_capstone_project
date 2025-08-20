import pandas as pd
from sklearn.linear_model import LinearRegression


# Linear regression function to calculate missing values for every column
def linear_regression(df_energy):
    # Create a copy of the DataFrame to avoid changing the original data
    df_filled = df_energy.copy()

    # Iterate through each column in the DataFrame
    for col in df_filled.columns:
        if col in ['country', 'year']:
            continue

        # Prepare the data for linear regression
        df_temp = df_filled[['year', col]].dropna()
        if df_temp.empty:
            continue

        X = df_temp[['year']]
        y = df_temp[col]

        # Fit the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict missing values
        missing_mask = df_filled[col].isnull()
        if missing_mask.any():
            predicted_values = model.predict(
                df_filled.loc[missing_mask, ['year']]
            )
            df_filled.loc[missing_mask, col] = predicted_values
    return df_filled


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


# Drop columns with more than 3% missing values
def drop_columns_with_high_missing_values(df_energy):
    def count_zeros(df):
        return (df == 0).mean() * 100
    nulls_energy = pd.Series(count_zeros(df_energy))
    columns_to_keep = nulls_energy[nulls_energy < 5].index.tolist()
    df_energy = df_energy[columns_to_keep]
    return df_energy


# Fill values of 0 with the mean of the rest of that column,
# for numeric columns only
def fill_remaining_nulls(df_energy):
    # Use linear regression to fill all remaining missing values
    df_energy = linear_regression(df_energy)
    # Set all numerical columns to 3dp
    df_energy = df_energy.round(3)
    return df_energy


def clean_energy(df_energy):
    df_energy = drop_unnecessary_columns(df_energy)
    df_energy = drop_records_outside_timeline(df_energy)
    df_energy = drop_columns_with_high_missing_values(df_energy)
    df_energy = fill_remaining_nulls(df_energy)
    return df_energy

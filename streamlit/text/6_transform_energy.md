### Transforming Energy Data
- The energy data was far more frustrating to work with
  - Years outside the range of 1994-2023 were dropped
  - Records without an 'iso_code' were removed, they were not individual countries
  - Countries that had no values were also removed
  - Due to the sheer volume of missing data, columns with over 5% missing values were dropped from the dataset
  - Further, columns that had no values from any individual country were also dropped
  - Any remaining nulls were filled using a linear regression model
### Transforming Energy Data
- The energy data was far more frustrating to work with
  - Years outside the range of 1994-2023 were dropped
  - Records without an 'iso_code' were removed, they were not individual countries
  - Countries that had no values were also removed
  - Due to the sheer volume of missing data, columns with over 5% missing values were dropped from the dataset
  - Further, columns that had no values from any individual country were also dropped
  - Any remaining nulls were filled using a linear regression model, this was used due to some problem in attempting to use other methods leaving null values in the dataset
- After these steps, while the data was cleaner, it was reduced in size to only 6 columns, 4 of which were already in the CO2 dataset
- However, when implementing this from jupyter notebook into my pipeline, I encountered some issues due to minor restructuring of my code, leaving upwards over 60 columns for the pipeline to handle
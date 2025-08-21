### Transforming CO2 Data
- Transforming the data was a mixed bag, but the data was explored with jupyter notebook first to find out what needed to be done
- CO2 data required straightforward cleaning and normalization
  - Years outside range of 1994-2023 were removed, they were the only years that all countries had data for
  - Nulls were handled by either removing the country if they contained no data, or had no data for a relevant column, or filling with the mean value for that country
  - No duplicate records were found
  - Some column types were changed to better reflect the data (e.g. float64 to int for year/gdp)
- After each of these steps were taken, I assessed the data and decided to drop any columns that still contained null values
- This resulted in a cleaner dataset with no missing values, and also a more concise dataset, moving from 79 columns, to 11 columns
- Finally, to enrich the CO2 data, regions were added as an additional column for better grouping, this was done because there were 253 countries and you'll see why thats a problem on my first page in the Streamlit app
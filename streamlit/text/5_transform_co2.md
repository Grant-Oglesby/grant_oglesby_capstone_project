### Transforming CO2 Data
- Transforming the data was a mixed bag, but the data was explored with jupyter notebook first to find out what needed to be done
- CO2 data required straightforward cleaning and normalization
  - Years outside range of 1994-2023 were removed, they were the only years that all countries had data for
  - Nulls were handled by either removing the country if they contained no data, or had no data for a relevant column, or filling with the mean value for that country
  - No duplicate records were found
  - Some column types were changed to better reflect the data (e.g. float64 to int for year/gdp)
- To enrich the CO2 data, regions were added as an additional column for better grouping, this was done because there were 253 countries
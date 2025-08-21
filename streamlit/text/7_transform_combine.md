### Combining the Datasets
- The CO2 and Energy datasets were merged on the 'country' and 'year' columns
- This resulted in a comprehensive dataset that included both CO2 emissions and energy consumption data for each country and year
- Any countries or years that were not present in both datasets were excluded from the final merged dataset
- Additionally, due to the code restructuring, the vast majority of columns were dropped from the energy dataset, allowing for a more concise analysis, and because my initial analysis exploration had not anticipated the additional columns
- The dataset was then saved to a new CSV file in 'data/transform' for loading
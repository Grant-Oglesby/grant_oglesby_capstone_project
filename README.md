# Grant Oglesby Capstone Project
Capstone project for Digital Futures Data Engineering Academy

## Initiative
To create a Streamlit application that will provide detailed analysis on historical data. The data used will be composed of global data, separated into countries and year, one dataset will contain information regarding CO2 and Greenhouse Gas emissions, the other will contain data regarding Energy statistics.

## Project Data Sources
- CO2 and Greenhouse Gas emissions data
  - https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv
- Energy statistics data
  - https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.csv

## Definition of Done
- All epics and user stories are implemented and tested
- Code is reviewed and meets quality standards
  - Unit tests are written and passing
  - End-to-end tests are written and passing
  - Code formatting is in accordance with PEP 8 guidelines
  - Code performance is optimized for time efficiency
- Documentation is complete and up-to-date
  - README.md is updated with project information
- Application is deployed and accessible to users
  - Users can access the application via a web browser
  - Users can interact with the data and visualizations
  - Application is responsive and performs well with large datasets

## Kanban Board
```mermaid
kanban
    EPICs
        (EPIC 1:
            As a Data Engineer/Scientist I want to analyze historical data on CO2 emissions and energy statistics so that I can gain insights into trends and patterns over time.
        )
        (EPIC 2:
            As a Data Engineer/Scientist I want to build a Streamlit application that allows users to interact with the data and visualize key metrics so that they can easily understand and analyze the information.
        )
        (EPIC 3:
            As a Data Engineer/Scientist I want to ensure the application is scalable and performant to handle large datasets so that it can provide real-time insights and support a growing user base.
        )
    User Stories
        (User Story 2:
            As a data engineer, I want to transform the extracted datasets into a suitable format so that I can remove any inconsistencies and ensure data quality.
                Task 1: Explore data in jupyter notebook
                Task 1.1: Identify null values and determine strategy
                Task 1.2: Identify duplicate records and determine strategy
                Task 1.3: Identify variable formats and determine strategy
                Task 1.4: Identify erroneous column typings and determine strategy
                Task 2: Identify enrichment opportunities
                Task 3: Create transformation functions to clean and format the data
                Task 4: Join data into a single dataset
                Task 5: Implement enrichment
                Task 5.1: TESTS - Create unit tests for data transformation
                Task 5.2: TESTS - Create end-to-end tests for data transformation
                Task 5.3: TESTS - Create performance tests for data transformation
        )
        (User Story 3:
            As a data engineer, I want to load the transformed datasets into a postgres database so that they can be easily accessed for analysis.
                Task 1: Setup database connection
                Task 2: Create tables and define schema
                Task 3: Load data into database
                Task 3.1: Create local csv file to stage data for testing purposes
                Task 4: Implement data validation checks
                Task 5: TESTS - Create unit tests for data loading
                Task 6: TESTS - Create end-to-end tests for data loading
                Task 7: TESTS - Create performance tests for data loading
        )
        (User Story 4:
            As a data engineer, I want to build a Streamlit application that allows users to interact with the data and visualize key metrics so that they can easily understand and analyze the information.
                Task 1: Explore data visualisation options in jupyter notebook
                Task 2: Setup Streamlit application
                Task 3: Create data visualization components in Streamlit
                Task 4: Implement responsive functionality in Streamlit
        )
    To Do (User Story 1:
            As a data engineer, I want to extract specific datasets as part of an automated ETL pipeline so that I can prepare the data for transforming.)
                Task 7: Record data extraction process
                Task 7.1: TESTS - Create end-to-end tests for data extraction
                Task 8: Implement data validation checks
                Task 8.1: TESTS - Create unit tests for data validation functions
        
    In Progress (User Story 1:
            As a data engineer, I want to extract specific datasets as part of an automated ETL pipeline so that I can prepare the data for transforming.)
                Task 6.1: TESTS - Create unit tests for data extraction functions

    Done (User Story 1:
            As a data engineer, I want to extract specific datasets as part of an automated ETL pipeline so that I can prepare the data for transforming.)
                Task 1: Create and clone git repository
                Task 2: Setup file system in accordance with ETL pipeline standards
                Task 3: Create and install pyproject.toml and requirements.txt
                Task 4: Setup .env.dev file to contain environment variables
                Task 5: Create run_etl.py to control ETL pipeline
                Task 6: Setup connection to call and receive source data

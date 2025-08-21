# Grant Oglesby Capstone Project
Capstone project for Digital Futures Data Engineering Academy

## Project Setup
The following instructions refer to the steps taken to set up and run the project on a Windows machine.
If you are using a different operating system, please refer to the appropriate documentation for your platform.
1. Clone the repository from the following link: https://github.com/Grant-Oglesby/grant_oglesby_capstone_project
2. Create a virtual environment
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment
   ```
   .venv\Scripts\activate
   ```
4. Install the required packages
   ```
   pip install -e .
   ```
5. Set up environment variables
   - Create a `.env.dev` file in the root directory of the project
   - Add the following environment variables to the `.env.dev` file:
     ```
     # Development environment variables

     # Source database configuration
     SOURCE_DB_NAME=
     SOURCE_DB_USER=
     SOURCE_DB_PASSWORD=
     SOURCE_DB_HOST=
     SOURCE_DB_PORT=

     # Target database configuration
     TARGET_DB_NAME=
     TARGET_DB_USER=
     TARGET_DB_PASSWORD=
     TARGET_DB_HOST=
     TARGET_DB_PORT=
     ```
   - Please enter your own details into the `.env.dev` file
6. Run the ETL pipeline from the project root directory
   ```
   run_etl dev
   ```
   - This will create the necessary tables and load the data into the target database, as well as create local files for the extracted data
7. Run the Streamlit application
   ```
   streamlit run streamlit/main.py
   ```

## Project Testing
Execute the following after completing project setup
```
run_tests unit
```
- Currently, only unit testing has been completed for the project
- Be aware that, due to errors, some tests overwrite datafiles and the ETL pipeline must be re-run to restore the original data

## Initiative
To create a Streamlit application that will provide detailed analysis on historical data. The data used will be composed of global data, separated into countries and year, one dataset will contain information regarding CO2 and Greenhouse Gas emissions, the other will contain data regarding Energy statistics.

## Project Data Sources
- CO2 and Greenhouse Gas emissions data
  - https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv
- Energy statistics data
  - https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.csv

## Project Optimisation
In the future, it would be a reasonable expectation to consider than the data sources used will be updated on a regular basis, with additional information being separated into country and year, as has been shown already implemented.
As such, the current ETL pipeline should be able to deal with these additional datasets with limited adjustment.
- Modify the script that selects 1994 to 2023 to instead capture the range of years that contain all countries with an iso_code.
- Modify the script drop all but required columns prior to cleaning implementations.
- Refer to columns to keep by their column name to prevent mishandling of data if the order of columns changes
These changes should allow for a more flexible handling of the data, as well as short run times of the ETL pipeline since the scope of the data would be limited prior to cleaning.

## Error Handling and Logging
While there has been limited implementation of error handling, in the form of 'try except', and no formal logging process, I believe that it would be beneficial to and relatively easy to include a logging framework in the future. This could include:
- Implementing more concise try-except blocks to catch and handle exceptions gracefully, rather than the broad catch-all approach currently in place
- Adding logging statements throughout the code to track the flow of execution and capture important events in a log file that can be reviewed later, currently this is done using print statements which are transient at best

## Security and Privacy Issues
In terms of security concerns, I would take the stance that there are only truly two main issues with the project, given that the only personal details used are my own.
- pyproject.toml - The toml file contains the ability to include the project owners name and email address, which could be a potential privacy concern if the file is shared publicly
  - This was addressed by using a email address that is not used for any purpose other than for informal communication
- .env.dev - The environment variables file contains the database connection details, which could be a security concern if the file is shared publicly
  - This was included in .gitignore to prevent it from being tracked by version control

## AWS Implementation
The project is not currently hosted on AWS, but it could be deployed to AWS in the future. This would involve:
- TRIGGER: Setting up AWS Workflow to trigger and manage the ETL pipeline on a schedule of once per year
- EXTRACT: Use of AWS Glue to retrieve the required datasets with https protocols
- TRANSFORM: Use of AWS Glue to clean and transform the data into a single cleaned dataset
- LOAD: Use of AWS Glue to load the cleaned dataset into the target data store on AWS S3
- VISUALISE: Use of AWS QuickSight to create visualizations and dashboards for the cleaned dataset
- ALTERNATE VISUALISE: Use of Streamlit as currently implemented and change the data source to the cleaned dataset in AWS S3, with appropriate credentials held in a secrets manager
This should allow for easy exploration and analysis of the data by end users and will require minimal resources, since the data is not expected to be updated significantly, beyond once per year.

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

    To Do 
                        
    In Progress 

    Done 
        (User Story 1:
            As a data engineer, I want to extract specific datasets as part of an automated ETL pipeline so that I can prepare the data for transforming.
                Task 1: Create and clone git repository
                Task 2: Setup file system in accordance with ETL pipeline standards
                Task 3: Create and install pyproject.toml and requirements.txt
                Task 4: Setup .env.dev file to contain environment variables
                Task 5: Create run_etl.py to control ETL pipeline
                Task 6: Setup connection to call and receive source data
                Task 6.1: TESTS - Create unit tests for data extraction functions
                Task 7: Record data extraction process
                Task 7.1: TESTS - Create end-to-end tests for data extraction
                Task 8: Implement data validation checks
                Task 8.1: TESTS - Create unit tests for data validation functions
        )
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
        )
        (User Story 3:
            As a data engineer, I want to load the transformed datasets into a postgres database so that they can be easily accessed for analysis.
                Task 1: Setup database connection
                Task 2: Create tables and define schema
                Task 3: Load data into database
                Task 3.1: Create local csv file to stage data for testing purposes
        )
        (User Story 4:
            As a data engineer, I want to build a Streamlit application that allows users to interact with the data and visualize key metrics so that they can easily understand and analyze the information.
                Task 1: Explore data visualisation options in jupyter notebook
                Task 2: Setup Streamlit application
                Task 3: Create data visualization components in Streamlit
                Task 4: Implement responsive functionality in Streamlit
        )
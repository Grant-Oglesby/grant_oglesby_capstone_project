import os
import sys
from src.extract.extract import extract_data
from config.env_config import setup_env
from src.transform.transform import transform_data
from src.load.load import load_dataframe_to_db
from src.load.load_database import get_engine


def main():
    try:
        # Set up environment
        setup_env(sys.argv)
        env = os.getenv("ENV", "unknown")
        print(f"Environment setup complete: {env}\n")

        # Begin pipeline
        print("Beginning ETL Pipeline\n")

        # Extract
        print("Beginning extraction")
        df_co2, df_energy = extract_data()
        print("Extraction completed\n")

        # Transform
        print("Beginning transformation")
        df_transformed = transform_data(df_co2, df_energy)
        print("Transformation completed\n")

        # Load
        print("Beginning loading")
        load_dataframe_to_db(df_transformed, get_engine())

        print(df_transformed.head())  # For demonstration purposes

    except Exception as e:
        print("Error: ETL Pipeline Failed")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

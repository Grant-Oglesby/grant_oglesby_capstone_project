import os
import sys
from src.extract.extract import extract_data
from config.env_config import setup_env


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
        extract_data()
        print("Extraction completed\n")

        # Transform

        # Load

    except Exception as e:
        print("Error: ETL Pipeline Failed")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

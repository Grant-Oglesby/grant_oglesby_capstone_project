import os
from dotenv import load_dotenv

# List of accepted environment variables
ENVS = ["dev", "test", "prod"]


# Function to set up the environment
# Heavily inspired by Ed Wright's walkthrough to setup environment
def setup_env(argv):
    # Confirms valid environment is provided
    if len(argv) != 2 or argv[1] not in ENVS:
        raise ValueError(
            "Please provide an environment: " f"{ENVS}. E.g. run_etl dev"
        )

    # Set the environment variable from the command line argument
    env = argv[1]

    # Clear previous environment variables and set new environment
    clear_previous_environment()
    os.environ["ENV"] = env

    # Redundant code as only accepted env variable is 'dev'
    env_file = ".env" if env == "prod" else f".env.{env}"

    # Raise an error if the environment file does not exist
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Environment file '{env_file}' not found")

    # Print statement to confirm environment setup successful
    print(f"Loading environment variables from: {env_file}")
    load_dotenv(env_file, override=True)


# Function to remove all previously setup environment variables
def clear_previous_environment():
    keys_to_clear = [
        "SOURCE_DB_NAME",
        "SOURCE_DB_USER",
        "SOURCE_DB_PASSWORD",
        "SOURCE_DB_HOST",
        "SOURCE_DB_PORT",
        "TARGET_DB_NAME",
        "TARGET_DB_USER",
        "TARGET_DB_PASSWORD",
        "TARGET_DB_HOST",
        "TARGET_DB_PORT",
    ]
    for key in keys_to_clear:
        if key in os.environ:
            del os.environ[key]

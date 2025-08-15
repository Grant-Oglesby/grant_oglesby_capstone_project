import os
from dotenv import load_dotenv

ENVS = ["dev", "test", "prod"]


def setup_env(argv):
    if len(argv) != 2 or argv[1] not in ENVS:
        raise ValueError(
            "Please provide an environment: " f"{ENVS}. E.g. run_etl dev"
        )

    env = argv[1]

    clear_previous_environment()
    os.environ["ENV"] = env

    env_file = ".env" if env == "prod" else f".env.{env}"

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Environment file '{env_file}' not found")

    print(f"Loading environment variables from: {env_file}")
    load_dotenv(env_file, override=True)


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

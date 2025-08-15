import os


def load_database_config():
    config = {
        "source_database": {
            "dbname": os.getenv("SOURCE_DB_NAME", "error"),
            "user": os.getenv("SOURCE_DB_USER", "error"),
            "password": os.getenv("SOURCE_DB_PASSWORD", ""),
            "host": os.getenv("SOURCE_DB_HOST", "error"),
            "port": os.getenv("SOURCE_DB_PORT", "5432"),
        },
        "target_database": {
            "dbname": os.getenv("TARGET_DB_NAME", "error"),
            "user": os.getenv("TARGET_DB_USER", "error"),
            "password": os.getenv("TARGET_DB_PASSWORD", ""),
            "host": os.getenv("TARGET_DB_HOST", "error"),
            "port": os.getenv("TARGET_DB_PORT", "5432"),
        },
    }

    return config

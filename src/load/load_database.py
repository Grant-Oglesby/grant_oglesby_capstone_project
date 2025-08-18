from config.db_config import load_database_config
from src.utils.db_utils import get_connection_details
# import sqlalchemy


# Retrieve target database details from .env.dev
def get_engine():
    try:
        # Load environment variables from .env.dev
        connection_details = load_database_config()['target_database']
        conn = get_connection_details(connection_details)
        return conn
    except Exception as e:
        print(f"Error occurred while getting database connection: {e}")
        return None

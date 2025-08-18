from sqlalchemy import create_engine


def create_db_engine(connection_details):
    engine = create_engine(
        f"postgresql+psycopg://{connection_details['user']}"
        f":{connection_details['password']}@{connection_details['host']}"
        f":{connection_details['port']}/{connection_details['dbname']}",
        connect_args={"options": "-csearch_path=de_2506_a"}
    )
    return engine


def get_connection_details(connection_details):
    engine = create_db_engine(connection_details)
    conn = engine.connect()
    return conn

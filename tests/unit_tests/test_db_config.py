import os
import pytest
from config.db_config import load_database_config, DatabaseConfigError


def test_load_database_config(mocker):
    # Mock variables
    mocker.patch.dict(os.environ, {
        "SOURCE_DB_NAME": "test_db",
        "SOURCE_DB_USER": "test_user",
        "SOURCE_DB_PASSWORD": "test_password",
        "SOURCE_DB_HOST": "test_host",
        "SOURCE_DB_PORT": "5432",
        "TARGET_DB_NAME": "target_db",
        "TARGET_DB_USER": "target_user",
        "TARGET_DB_PASSWORD": "target_password",
        "TARGET_DB_HOST": "target_host",
        "TARGET_DB_PORT": "5432"
    })

    config = load_database_config()

    # Assert all source database config values match mock
    assert config['source_database']["dbname"] == "test_db"
    assert config['source_database']["user"] == "test_user"
    assert config['source_database']["password"] == "test_password"
    assert config['source_database']["host"] == "test_host"
    assert config['source_database']["port"] == "5432"
    assert config['target_database']["dbname"] == "target_db"
    assert config['target_database']["user"] == "target_user"
    assert config['target_database']["password"] == "target_password"
    assert config['target_database']["host"] == "target_host"
    assert config['target_database']["port"] == "5432"


def test_load_database_config_missing_port_variable(mocker):
    # Mock variables with missing user value
    mocker.patch.dict(os.environ, {
        "SOURCE_DB_NAME": "test_db",
        "SOURCE_DB_USER": "test_user",
        "SOURCE_DB_PASSWORD": "test_password",
        "SOURCE_DB_HOST": "test_host",
        # "SOURCE_DB_PORT": "5432",
        "TARGET_DB_NAME": "target_db",
        "TARGET_DB_USER": "target_user",
        "TARGET_DB_PASSWORD": "target_password",
        "TARGET_DB_HOST": "target_host",
        "TARGET_DB_PORT": "5432"
    })

    config = load_database_config()

    # Assert all source database config values match mock
    assert config['source_database']["dbname"] == "test_db"
    assert config['source_database']["user"] == "test_user"
    assert config['source_database']["password"] == "test_password"
    assert config['source_database']["host"] == "test_host"
    assert config['source_database']["port"] == "5432"
    assert config['target_database']["dbname"] == "target_db"
    assert config['target_database']["user"] == "target_user"
    assert config['target_database']["password"] == "target_password"
    assert config['target_database']["host"] == "target_host"
    assert config['target_database']["port"] == "5432"


# Map from env variables names to keys
env_var_to_key = {
    "SOURCE_DB_NAME": "dbname",
    "SOURCE_DB_USER": "user",
    "SOURCE_DB_HOST": "host"
}


@pytest.mark.parametrize("env_var", [
    "SOURCE_DB_NAME",
    "SOURCE_DB_USER",
    "SOURCE_DB_HOST"
])
def test_load_database_config_missing_required_variable(env_var, mocker):
    # Mock with one var set to error
    mock_env = {
        'SOURCE_DB_NAME': 'test_source_db',
        'SOURCE_DB_USER': 'test_user',
        'SOURCE_DB_PASSWORD': 'test_password',
        'SOURCE_DB_HOST': 'localhost',
        'SOURCE_DB_PORT': '5432',
        'TARGET_DB_NAME': 'test_target_db',
        'TARGET_DB_USER': 'test_user',
        'TARGET_DB_PASSWORD': 'test_password',
        'TARGET_DB_HOST': 'localhost',
        'TARGET_DB_PORT': '5432'
    }
    mock_env[env_var] = "error"
    mocker.patch.dict(os.environ, mock_env)

    config_key = env_var_to_key[env_var]

    with pytest.raises(DatabaseConfigError, match=(
        f"Configuration error: source_database {config_key} is set to 'error'"
    )):
        load_database_config()

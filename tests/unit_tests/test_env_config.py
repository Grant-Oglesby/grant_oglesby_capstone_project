import os
import pytest
from unittest.mock import patch
from config.env_config import setup_env, clear_previous_environment


# Test file not found for .env.dev if missing
@patch("os.path.exists")
def test_setup_env_file_not_found_dev(mock_exists):
    mock_exists.return_value = False
    with pytest.raises(
        FileNotFoundError, match="Environment file '.env.dev' not found"
    ):
        setup_env(["script_name", "dev"])


# Test file not found for .env.test if missing
@patch("os.path.exists")
def test_setup_env_file_not_found_test(mock_exists):
    mock_exists.return_value = False
    with pytest.raises(
        FileNotFoundError, match="Environment file '.env.test' not found"
    ):
        setup_env(["script_name", "test"])


# Test for invalid environment variable
def test_setup_env_invalid_env():
    with pytest.raises(ValueError, match="Please provide an environment"):
        setup_env(["script_name", "invalid_env"])


# Test for missing environment variable
def test_setup_env_missing_variable():
    with pytest.raises(ValueError, match="Please provide an environment"):
        setup_env(["script_name"])


# Test for too many environment arguments
def test_setup_env_too_many_arguments():
    with pytest.raises(ValueError, match="Please provide an environment"):
        setup_env(["script_name", "dev", "extra"])


# Test clearing previous environment variables
def test_clear_previous_environment_variables():
    test_vars = {
        "SOURCE_DB_NAME": "test_db",
        "SOURCE_DB_USER": "test_user",
        "TARGET_DB_NAME": "target_db",
        "UNRELATED_VAR": "should_remain",
    }

    for key, value in test_vars.items():
        os.environ[key] = value

    clear_previous_environment()

    assert "SOURCE_DB_NAME" not in os.environ
    assert "SOURCE_DB_USER" not in os.environ
    assert "TARGET_DB_NAME" not in os.environ
    assert "UNRELATED_VAR" in os.environ

    if "UNRELATED_VAR" in os.environ:
        del os.environ["UNRELATED_VAR"]


@patch("config.env_config.load_dotenv")
@patch("os.path.exists")
def test_load_dotenv(mock_exists, mock_load_dotenv, mocker):
    # Setup mock variables for testing
    mock_exists.return_value = True
    mocker.patch("config.env_config.clear_previous_environment")

    setup_env(["script_name", "dev"])
    mock_load_dotenv.assert_called_once_with(".env.dev", override=True)


@patch("os.path.exists")
def test_setup_env_file_not_found(mock_exists, mocker):
    mock_exists.return_value = False
    mocker.patch("config.env_config.clear_previous_environment")

    with pytest.raises(
        FileNotFoundError, match="Environment file '.env.dev' not found"
    ):
        setup_env(["script_name", "dev"])

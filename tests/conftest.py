import pytest
import os
from config.env_config import setup_env


def ensure_test_environment():
    env = os.environ.get("ENV")
    if env is None or env == 'test':
        setup_env(["pytest", "test"])


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    ensure_test_environment()
    yield

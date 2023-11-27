import pytest
from src.insights.jobs import ProcessJobs


@pytest.fixture(scope="function", autouse=True)
def clear_cache():
    process_instance = ProcessJobs()
    process_instance.result = []

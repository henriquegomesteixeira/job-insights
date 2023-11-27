from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    assert isinstance(result, list)
    assert all(isinstance(job, dict) for job in result)

    keys = result[0].keys() if result else []
    expected_keys = {"title", "salary", "type"}
    assert all(key in expected_keys for key in keys)

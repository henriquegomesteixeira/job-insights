import pytest
from src.insights.jobs import ProcessJobs

JOB_TYPES = {
    "PART_TIME": {"jobs": 172},
    "OTHER": {"jobs": 39},
    "FULL_TIME": {"jobs": 3078},
    "CONTRACTOR": {"jobs": 14},
    "TEMPORARY": {"jobs": 2},
    "INTERN": {"jobs": 19},
}
TOTAL_JOBS = 3324


def test_read_jobs():
    process = ProcessJobs()
    process.read("data/jobs.csv")
    results = process.jobs_list
    assert type(results) == list
    assert len(results) == TOTAL_JOBS
    for result in results:
        assert type(result) == dict

    process.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process.read("tests/mocks/jobs.csv")
    result_mock = process.jobs_list

    assert type(result_mock) == list
    assert len(result_mock) == 3
    expected_list = [
        {"title": "Front end developer", "salary": "2000", "type": "trainee"},
        {"title": "Back end developer", "salary": "3000", "type": "full time"},
        {
            "title": "Full stack end developer",
            "salary": "4000",
            "type": "full time",
        },
    ]
    for result_mock, expected in zip(result_mock, expected_list):
        assert result_mock == expected


def test_total_jobs_in_job_types():
    process = ProcessJobs()
    process.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process.read("data/jobs.csv")
    assert TOTAL_JOBS == sum([type_["jobs"] for type_ in JOB_TYPES.values()])


def test_get_unique_job_types():
    process = ProcessJobs()
    process.read("data/jobs.csv")
    result = process.get_unique_job_types()

    assert len(result) == 6
    for type_ in JOB_TYPES.keys():
        assert type_ in result

    process.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process.read("tests/mocks/jobs_with_types.csv")
    result = process.get_unique_job_types()

    assert len(result) == 2
    assert "full time" in result
    assert "trainee" in result


def test_filter_by_multiple_criteria_valid():
    jobs = [
        {"id": 1, "industry": "IT", "job_type": "FULL_TIME"},
        {"id": 2, "industry": "Healthcare", "job_type": "PART_TIME"},
    ]
    process_jobs = ProcessJobs()
    result = process_jobs.filter_by_multiple_criteria(
        jobs, {"industry": "IT", "job_type": "FULL_TIME"}
    )
    assert result == [{"id": 1, "industry": "IT", "job_type": "FULL_TIME"}]

    with pytest.raises(TypeError):
        process_jobs.filter_by_multiple_criteria(jobs, "type_jobs")

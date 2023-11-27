import pytest
from src.insights.salaries import ProcessSalaries

TOTAL_JOBS_WITH_SPECIFIED_SALARY = 2232
MAX_SALARY = 383416
MIN_SALARY = 19857


import pytest
from src.insights.salaries import ProcessSalaries

TOTAL_JOBS_WITH_SPECIFIED_SALARY = 2232
MAX_SALARY = 383416
MIN_SALARY = 19857


def test_get_max_salary():
    process_salaries = ProcessSalaries()
    process_salaries.read("data/jobs.csv")
    assert process_salaries.get_max_salary() == MAX_SALARY

    process_salaries.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process_salaries.read("tests/mocks/jobs_with_salaries.csv")
    assert process_salaries.get_max_salary() == 8000


def test_get_min_salary():
    process_salaries = ProcessSalaries()
    process_salaries.read("data/jobs.csv")
    assert process_salaries.get_min_salary() == MIN_SALARY

    process_salaries.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process_salaries.read("tests/mocks/jobs_with_salaries.csv")
    assert process_salaries.get_min_salary() == 1000


def test_matches_salary_range():
    invalid_jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": -1, "min_salary": 10},
    ]
    jobs = [
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 1500, "min_salary": 0},
    ]
    salaries = [0, 1, 5, 1000, 2000, -1, -2]
    expected = [
        [False, False, False, True, True, False, False],
        [True, True, True, True, False, False, False],
    ]

    for job in invalid_jobs:
        for salary in salaries:
            with pytest.raises(ValueError):
                ProcessSalaries().matches_salary_range(job, salary)

    for job_index in range(len(jobs)):
        for salary_index in range(len(salaries)):
            result = ProcessSalaries().matches_salary_range(
                jobs[job_index], salaries[salary_index]
            )
            assert result == expected[job_index][salary_index]

    # ? Valida que pode ser passada uma string numérica
    assert ProcessSalaries().matches_salary_range(jobs[1], "5") is True
    assert ProcessSalaries().matches_salary_range(jobs[1], "1800") is False

    invalid_types = [None, "", "aloha", [], {}, lambda: 1]
    for invalid in invalid_types:
        with pytest.raises(ValueError):
            ProcessSalaries().matches_salary_range(
                {"max_salary": "1000", "min_salary": invalid}, 20
            )
        with pytest.raises(ValueError):
            ProcessSalaries().matches_salary_range(
                {"min_salary": "1000", "max_salary": invalid}, 20
            )
        with pytest.raises(ValueError):
            ProcessSalaries().matches_salary_range(
                {"min_salary": "100", "max_salary": "1000"}, invalid
            )
    with pytest.raises(ValueError):
        ProcessSalaries().matches_salary_range({"max_salary": "1000"}, 10)
    with pytest.raises(ValueError):
        ProcessSalaries().matches_salary_range({"min_salary": "1000"}, 10)


def test_filter_by_salary_range():
    jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": -1, "min_salary": 10},
    ]
    salaries = [0, 1, 5, 1000, 2000, -1, -2, None, "", [], {}, lambda: 1]
    expected: list[list[dict]] = [
        [jobs[3], jobs[4]],  # 0
        [jobs[3], jobs[4]],  # 1
        [jobs[3], jobs[4]],  # 5
        [jobs[2], jobs[3], jobs[4]],  # 1000
        [jobs[2], jobs[3]],  # 2000
        [],  # -1
        [],  # -2
        [],  # None
        [],  # ""
        [],  # []
        [],  # {}
        [],  # lambda: 1
    ]
    for salary_index in range(len(salaries)):
        assert (
            ProcessSalaries().filter_by_salary_range(
                jobs, salaries[salary_index]
            )
            == expected[salary_index]
        )

    # ? Valida que pode ser passada uma string numérica
    assert ProcessSalaries().filter_by_salary_range(jobs, "5") == expected[2]
    assert (
        ProcessSalaries().filter_by_salary_range(jobs, "1000") == expected[3]
    )
    for salary_index in range(len(salaries)):
        assert ProcessSalaries().filter_by_salary_range(
            [
                {
                    "max_salary": str(job["max_salary"]),
                    "min_salary": str(job["min_salary"]),
                }
                for job in jobs
            ],
            salaries[salary_index],
        ) == [
            {
                "max_salary": str(job["max_salary"]),
                "min_salary": str(job["min_salary"]),
            }
            for job in expected[salary_index]
        ]

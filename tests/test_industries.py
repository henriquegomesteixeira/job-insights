import pytest
from src.insights.industries import ProcessIndustries


INDUSTRIES = {
    "Health Care": {"jobs": 232},
    "Arts, Entertainment & Recreation": {"jobs": 2},
    "Biotech & Pharmaceuticals": {"jobs": 317},
    "Agriculture & Forestry": {"jobs": 1},
    "Consumer Services": {"jobs": 7},
    "Accounting & Legal": {"jobs": 29},
    "Insurance": {"jobs": 29},
    "Restaurants, Bars & Food Services": {"jobs": 3},
    "Non-Profit": {"jobs": 10},
    "Transportation & Logistics": {"jobs": 8},
    "Business Services": {"jobs": 583},
    "Retail": {"jobs": 63},
    "Aerospace & Defense": {"jobs": 144},
    "Construction, Repair & Maintenance": {"jobs": 66},
    "Media": {"jobs": 29},
    "Real Estate": {"jobs": 5},
    "Finance": {"jobs": 223},
    "Information Technology": {"jobs": 679},
    "Education": {"jobs": 60},
    "Telecommunications": {"jobs": 35},
    "Manufacturing": {"jobs": 42},
    "Government": {"jobs": 105},
    "Oil, Gas, Energy & Utilities": {"jobs": 28},
}
UNINFORMED_INDUSTRIES = 624
TOTAL_JOBS = 3324
TOTAL_JOBS_WITH_SPECIFIED_SALARY = 2232
MAX_SALARY = 383416
MIN_SALARY = 19857


def test_total_jobs_in_industries():
    process_industries = ProcessIndustries()
    process_industries.read("data/jobs.csv")

    assert TOTAL_JOBS - UNINFORMED_INDUSTRIES == sum(
        [industry["jobs"] for industry in INDUSTRIES.values()]
    )


def test_get_unique_industries():
    process_industries = ProcessIndustries()
    process_industries.read("data/jobs.csv")
    result = process_industries.get_unique_industries()

    assert len(result) == len(INDUSTRIES)

    for industry in INDUSTRIES:
        assert industry in result

    process_industries.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process_industries.read("tests/mocks/jobs_with_industries.csv")
    result = process_industries.get_unique_industries()

    assert len(result) == 2
    assert "agriculture" in result
    assert "solar energy" in result

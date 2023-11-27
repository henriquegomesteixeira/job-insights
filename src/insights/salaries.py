from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for salary in self.jobs_list:
            if (
                salary["max_salary"] != ""
                and salary["max_salary"] != "invalid"
            ):
                if int(salary["max_salary"]) > max_salary:
                    max_salary = int(salary["max_salary"])
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for salary in self.jobs_list:
            if (
                salary["min_salary"] != ""
                and salary["min_salary"] != "invalid"
            ):
                if int(salary["min_salary"]) < min_salary:
                    min_salary = int(salary["min_salary"])
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            salary_u = int(salary)

            if (
                min_salary == "" or max_salary == ""
                or min_salary > max_salary
            ):
                raise ValueError()

            if salary_u <= max_salary and salary_u >= min_salary:
                return True
            else:
                return False

        except (TypeError, ValueError, KeyError):
            raise ValueError

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_list = list()

        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filtered_list.append(job)
            except ValueError:
                continue
        return filtered_list

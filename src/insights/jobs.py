from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self,) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = list()
        for job in self.jobs_list:
            job_types.append(job["job_type"])
        return list(set(job_types))

    def filter_by_multiple_criteria(self, jobs, filter_criteria) -> List[dict]:
        filtered_list = list()
        for job in jobs:
            if (
                job["job_type"] == filter_criteria["job_type"]
                and job["industry"] == filter_criteria["industry"]
            ):
                filtered_list.append(job)
        return filtered_list

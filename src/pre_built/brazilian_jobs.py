from typing import List, Dict
from src.insights.jobs import ProcessJobs


def read_brazilian_file(path: str) -> List[Dict]:
    """Reads a portuguese file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    process = ProcessJobs()
    process.read(path)

    result = process.jobs_list

    for job in result:
        job["title"] = job.pop("titulo")
        job["salary"] = job.pop("salario")
        job["type"] = job.pop("tipo")

    return result

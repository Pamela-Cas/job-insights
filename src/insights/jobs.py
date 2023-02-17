import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    with open(path) as file:
        jobList = csv.DictReader(file)

        return list(jobList)


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_types = read(path)
    return list(set([job["job_type"] for job in jobs_types]))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_by_type = []
    for job in jobs:
        if job["job_type"] != "" and job["job_type"] == job_type:
            filter_by_type.append(job)
    return filter_by_type

# aprendido na mentoria!!!
from jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    industries = set()

    for job in read(path):
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError

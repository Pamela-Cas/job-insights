from src.insights.jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    industries = set()
    for job in read(path):
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:  
    industries_filter = []

    for item in jobs:
        if item['industry'] == industry:
            industries_filter.append(item)

    return industries_filter

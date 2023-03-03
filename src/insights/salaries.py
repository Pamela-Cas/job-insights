from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    result = read(path)
    salary = set()

    for item in result:
        if item['max_salary'].isdigit():
            salary.add(int(item['max_salary']))

    return max(salary)
# https://acervolima.com/python-string-isdigit-e-seu-aplicativo/


def get_min_salary(path: str) -> int:
    resultList = read(path)
    salary = set()
    for item in resultList:
        if item['min_salary'].isdigit():
            salary.add(int(item['min_salary']))

    return min(salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError(
                "Não existe chave 'min_salary' ou 'max_salary'"
            )
        if int(job['min_salary']) > int(job['max_salary']):
            raise ValueError
        int(salary)
    except Exception:
        raise ValueError(
            "O valor de min_salary deve ser menor que o o valor de max_salary"
        )

    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])
    pass


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    filtered_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_list.append(job)
        except ValueError:
            pass
    return filtered_list

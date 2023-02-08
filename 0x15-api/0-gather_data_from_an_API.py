#!/usr/bin/python3
""" REST api script """


import requests
from sys import argv


def main(employee_id):
    url = "https://jsonplaceholder.typicode.com/todos?userId={}" \
        .format(employee_id)
    response = requests.get(url)
    todos = response.json()

    url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    response = requests.get(url)
    user = response.json()
    EMPLOYEE_NAME = user['name']

    completed_tasks = \
        [TASK_TITLE["title"]
            for TASK_TITLE in todos if TASK_TITLE["completed"]]
    TOTAL_NUMBER_OF_TASKS = len(todos)
    NUMBER_OF_DONE_TASKS = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    employee_id = int(argv[1])
    main(employee_id)

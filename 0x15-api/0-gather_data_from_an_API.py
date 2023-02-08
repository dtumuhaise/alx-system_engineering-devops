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
    name = user['name']

    completed_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    employee_id = int(argv[1])
    main(employee_id)

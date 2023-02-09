#!/usr/bin/python3
""" REST api script """


import requests
from sys import argv


def main(userId):
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}" \
        .format(userId)
    response = requests.get(todo_url)
    todos = response.json()

    users_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(userId)
    response = requests.get(users_url)
    user = response.json()
    EMPLOYEE_NAME = user['name']

    completed_tasks = \
        [TASK_TITLE["title"]
            for TASK_TITLE in todos if TASK_TITLE["completed"]]
    TOTAL_NUMBER_OF_TASKS = len(todos)
    NUMBER_OF_DONE_TASKS = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for TASK_TITLE in completed_tasks:
        print("\t {}".format(TASK_TITLE))


if __name__ == "__main__":
    userId = int(argv[1])
    if userId <= 10:
        main(userId)
    else:
        print("user doesnt exist")

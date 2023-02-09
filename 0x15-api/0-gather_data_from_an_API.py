#!/usr/bin/python3
""" REST api script """


# import requests
# from sys import argv


# def main(userId):
#     todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}" \
#         .format(userId)
#     response = requests.get(todo_url)
#     todos = response.json()

#     users_url = "https://jsonplaceholder.typicode.com/users/{}" \
#         .format(userId)
#     response = requests.get(users_url)
#     user = response.json()
#     EMPLOYEE_NAME = user['name']

#     completed_tasks = \
#         [TASK_TITLE["title"]
#             for TASK_TITLE in todos if TASK_TITLE["completed"]]
#     TOTAL_NUMBER_OF_TASKS = len(todos)
#     NUMBER_OF_DONE_TASKS = len(completed_tasks)

#     print("Employee {} is done with tasks({}/{}):".format(
#         EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
#     for TASK_TITLE in completed_tasks:
#         print("\t {}".format(TASK_TITLE))


# if __name__ == "__main__":
#     userId = int(argv[1])
#     main(userId)

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]

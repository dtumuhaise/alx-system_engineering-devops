#!/usr/bin/python3
""" REST api script """


import requests
from sys import argv


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

if __name__ == "__main__":
    data = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks = []
    data2 = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            EMPLOYEE_NAME = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

            if i.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
                                                        EMPLOYEE_NAME,
                                                        NUMBER_OF_DONE_TASKS,
                                                        TOTAL_NUMBER_OF_TASKS))

    for i in tasks:
        print("\t {}".format(i))

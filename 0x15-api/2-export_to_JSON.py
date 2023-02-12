#!/usr/bin/python3
"""export as json"""


import json
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
    username = user.get('username')

    data = {"{}".format(userId): [{"task": TASK_TITLE.get("title"),
                                  "completed": TASK_TITLE.get("completed"),
                                   "username": username}
                                  for TASK_TITLE in todos]}

    with open("{}.json".format(userId), "w", newline="") as file:
        json.dump(data, file)


if __name__ == "__main__":
    userId = int(argv[1])
    if userId <= 10:
        main(userId)
    else:
        print("user doesnt exist")

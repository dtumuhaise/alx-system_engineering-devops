#!/usr/bin/python3
"""export as json"""


import json
import requests
from sys import argv


def main():
    data = {}
    for userId in range(1, 11):
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}" \
            .format(userId)
        response = requests.get(todo_url)
        todos = response.json()

        users_url = "https://jsonplaceholder.typicode.com/users/{}" \
            .format(userId)
        response = requests.get(users_url)
        user = response.json()
        username = user.get('username')

        tasks = [{"task": task.get("title"),
                 "completed": task.get("completed"),
                  "username": username} for task in todos]
        data[userId] = tasks

        with open("todo_all_employees.json", "w", newline="") as file:
            json.dump(data, file)


if __name__ == "__main__":
    main()

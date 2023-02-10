#!/usr/bin/python3
""" export data in CSV format """


import csv
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

    with open("{}.csv".format(userId), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [userId, username, todo.get("completed"), todo.get("title")])


if __name__ == "__main__":
    userId = int(argv[1])
    if userId <= 10:
        main(userId)
    else:
        print("user doesnt exist")

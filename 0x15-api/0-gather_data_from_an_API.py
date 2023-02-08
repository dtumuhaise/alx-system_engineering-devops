#!/usr/bin/python3
""" REST api script """


import requests
from sys import argv


def main():
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(argv[1]))
    users = response.json()

    response = requests.get(url + "todos", params={"userId": argv[1]})
    todos = response.json()

    completed_tasks = [tasks.get("title")
                       for tasks in todos if tasks.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        users.get("name"), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    main()

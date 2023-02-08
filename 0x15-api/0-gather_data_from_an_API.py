#!/usr/bin/python3
""" REST api script """


import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com/todos/"


def get_employee_name(employee_id):
    """get the employee name """

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    employee = response.json()
    return employee['name']


def get_todo_list_progress(employee_id):
    """get todolist progress"""

    response = requests.get("{}?userId={}".format(url, employee_id))
    todos = response.json()
    completed_tasks = [task for task in todos if task['completed']]
    return completed_tasks


def main(employee_id):
    """ main function """

    employee_name = get_employee_name(employee_id)
    todo_list_progress = get_todo_list_progress(employee_id)
    completed_task_count = len(todo_list_progress)
    total_task_count = len(todos)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_task_count, total_task_count))
    for task in todo_list_progress:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    employee_id = int(argv[1])
    main(employee_id)

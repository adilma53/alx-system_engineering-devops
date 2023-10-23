#!/usr/bin/python3
"""gather data from api using user id"""
import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        baseUrl+f"{uid}"
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={uid}"
    ).json()

    task_completed = [
        task.get("title") for task in todos if task.get("completed") is True
    ]
    print(
        f"Employee {user.get('name')} is done with tasks({len(task_completed)}/{len(todos)}):")
    [print("\t {}".format(task)) for task in task_completed]

#!/usr/bin/python3
"""gather data from api using user id"""
import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    ).json()

    task_completed = [
        task.get("title") for task in todos if task.get("completed") is True
    ]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(task_completed), len(todos)
        )
    )
    [print("\t {}".format(task)) for task in task_completed]

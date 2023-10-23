#!/usr/bin/python3
"""Returns to do list info"""


import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    ).json()

    task_completed = [
        task.get("title") for task in todos if task.get("completed") is True
    ]
    print(
        f"Employee {user.get("name")} is done with tasks({len(task_completed)}/{len(todos)}):"
    )
    [print(f"\t {task}") for task in task_completed]

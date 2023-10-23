#!/usr/bin/python3
"""write todos for a specific user into a json"""

import json
import requests
import sys


if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/"
    uid = sys.argv[1]
    user = requests.get(baseUrl + f"users/{uid}").json()
    username = user.get("username")
    todos = requests.get(baseUrl + f"todos?userId={uid}").json()

    with open(f"{uid}.json", "w") as file:
        json.dump(
            {
                uid: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username,
                    }
                    for task in todos
                ]
            },
            file,
        )

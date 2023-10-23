#!/usr/bin/python3
"""export all users todos to a json"""

import json
import requests


if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/"
    users = requests.get(baseUrl + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump(
            {
                user.get("id"): [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user.get("username"),
                    }
                    for task in requests.get(
                        baseUrl + "todos", params={"userId": user.get("id")}
                    ).json()
                ]
                for user in users
            },
            file,
        )

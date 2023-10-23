#!/usr/bin/python3
"""write todos to csv file"""

import csv
import requests
import sys


if __name__ == "__main__":

    uid = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = requests.get(baseUrl + f"users/{uid}").json()
    username = user.get("username")
    todos = requests.get(baseUrl + f"todos?userId={uid}").json()

    with open(f"{uid}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [
            writer.writerow(
                [
                    uid, username, task.get("completed"), task.get("title")
                ]
            ) for task in todos
        ]

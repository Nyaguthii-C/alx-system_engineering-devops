#!/usr/bin/python3
"""
Python script to export data from task 0 in the json format
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    USERS = requests.get(url + "/users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "username": u.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            } for task in requests.get(url + "/todos",
                                       params={"userId": u.get("id")}).json()]
            for u in USERS}, jsonfile)

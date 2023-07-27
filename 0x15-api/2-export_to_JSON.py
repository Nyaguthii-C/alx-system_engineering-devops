#!/usr/bin/python3
"""
Python script to export data from task 0 in the json format
"""

import json
import requests
import sys

if __name__ == "__main__":
    USER_ID_select = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    USER_ID_url = url + "/{}".format(USER_ID_select)
    USER_ID = requests.get(USER_ID_url).json().get("id")
    USERNAME_url = url + "/{}".format(USER_ID)
    USERNAME = requests.get(USERNAME_url).json().get("username")
    tasks_url = url + "/{}/todos".format(USER_ID)
    tasks = requests.get(tasks_url).json()
    with open('{}.json'.format(USER_ID), 'w', newline='') as jsonfile:
        json.dump({USER_ID: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": USERNAME,
                } for task in tasks]}, jsonfile)

#!/usr/bin/python3
"""
Python script to export data from task 0 in the CSV format
"""

import csv
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
    with open('{}.csv'.format(USER_ID), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [USER_ID, USERNAME, task.get("completed"), task.get("title")])
            for task in tasks]

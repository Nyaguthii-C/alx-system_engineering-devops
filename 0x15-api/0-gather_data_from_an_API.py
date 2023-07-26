#!/usr/bin/python3

"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    tasks_url = url + "/user/{}/todos".format(sys.argv[1])
    tasks_data = requests.get(tasks_url)
    tasks = tasks_data.json()
    name_url = url + "/users/{}".format(sys.argv[1])
    name_data = requests.get(name_url)
    name = name_data.json()

    total_tasks = len(tasks)
    done_task = len([task for task in tasks if task.get("completed")])
    name_url = url + "/users/{}".format(sys.argv[1])
    employee_name = name.get("name")
    print("Employee {} is done with tasks {}/{}:"
          .format(employee_name, done_task, total_tasks))
    for task in tasks:
        if (task.get("completed")):
            print("\t{}".format(task.get("title")))

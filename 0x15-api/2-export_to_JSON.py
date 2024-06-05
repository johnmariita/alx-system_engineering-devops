#!/usr/bin/python3
"""
Script that creates a json file of a user's
TODO progress
"""

import csv
import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    user_url = 'https://jsonplaceholder.typicode.com/users/'

    with urlopen(todo_url) as response:
        body = response.read()

    user_url += sys.argv[1]
    with urlopen(user_url) as users_res:
        users = users_res.read()

    emps = json.loads(body)
    users_json = json.loads(users)
    name = users_json['name']
    filename = sys.argv[1] + '.json'

    with open(filename, 'w') as file:
        tasks = []
        t_dict = {}
        for task in emps:
            task_dict = {}
            if task['userId'] == int(sys.argv[1]):
                task_dict['task'] = task['title']
                task_dict['completed'] = task['completed']
                task_dict['username'] = users_json['username']
                tasks.append(task_dict)

        t_dict[sys.argv[1]] = tasks
        json.dump(t_dict, file)

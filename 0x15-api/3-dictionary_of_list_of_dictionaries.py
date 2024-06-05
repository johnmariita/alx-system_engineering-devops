#!/usr/bin/python3
"""
Script that creates a json file of a user's
TODO progress
"""

import csv
import json
from urllib.request import urlopen


if __name__ == "__main__":
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    user_url = 'https://jsonplaceholder.typicode.com/users/'

    with urlopen(todo_url) as response:
        body = response.read()

    todos = json.loads(body)

    with urlopen(user_url) as response:
        total_users = response.read()

    total_users_json = json.loads(total_users)

    total_todos = {}
    with open('todo_all_employees.json', 'w') as file:
        for i in range(1, len(total_users_json) + 1):
            tasks = []
            tasks_dict = {}
            userN = i
            this_user_url = user_url + str(userN)

            with urlopen(this_user_url) as res:
                user_body = json.loads(res.read())

            for emp in todos:
                if emp['userId'] == userN:
                    tasks_dict['username'] = user_body['username']
                    tasks_dict['task'] = emp['title']
                    tasks_dict['completed'] = emp['completed']
                tasks.append(tasks_dict)

            total_todos[str(userN)] = tasks

        json.dump(total_todos, file)

#!/usr/bin/python3
"""
CSV for employees result
"""

import requests
import sys


if __name__ == '__main__':
    emp_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users"
    url = user_url + "/" + emp_id

    response = requests.get(url)
    name = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open(f'{emp_id}.csv', 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(emp_id, name, task.get('completed'),
                               task.get('title')))

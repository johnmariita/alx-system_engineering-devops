#!/usr/bin/python3
"""
Exporting employee results to JSON
"""

import json
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

    emp_dict = {emp_id: []}
    for task in tasks:
        emp_dict[emp_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "uername": name
        })
    with open(f'{emp_id}.json', 'w') as filename:
        json.dump(emp_dict, filename)

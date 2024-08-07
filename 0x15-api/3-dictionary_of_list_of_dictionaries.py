#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    emp_dict = {}
    for user in users:
        emp_id = user.get('id')
        username = user.get('username')
        url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        emp_dict[emp_id] = []
        for task in tasks:
            emp_dict[emp_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(emp_dict, file)

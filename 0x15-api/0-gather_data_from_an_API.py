#!/usr/bin/python3
"""
Using jsonplaceholder to return the TODO list
progress of an employee
"""

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
    empN = []
    completed = 0

    for emp in emps:
        if emp['userId'] == int(sys.argv[1]):
            if emp['completed'] is True:
                completed += 1
                empN.append(emp)

    print(f"Employee {users_json['name']} is done with tasks({completed}/20):")
    for e in empN:
        print(f"     {e['title']}")

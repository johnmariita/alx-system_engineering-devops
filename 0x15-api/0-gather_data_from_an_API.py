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
    ct = 0
    tasks = 0

    for emp in emps:
        if emp['userId'] == int(sys.argv[1]):
            tasks += 1
            if emp['completed'] is True:
                ct += 1
                empN.append(emp)

    print(f"Employee {users_json['name']} is done with tasks({ct}/{tasks}):")
    for e in empN:
        print(f"     {e['title']}")

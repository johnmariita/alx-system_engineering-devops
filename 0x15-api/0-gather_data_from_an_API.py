#!/usr/bin/python3
"""
python script REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import sys
import urllib.request

if __name__ == "__main__":
    emp_id = sys.argv[1]
    name = ""
    user_url = "https://jsonplaceholder.typicode.com/users/" + emp_id
    todo_url = user_url + "/todos"

    with urllib.request.urlopen(user_url) as resp:
        details = resp.read().decode('utf-8')
        details = json.loads(details)
        name = details['name']

    with urllib.request.urlopen(todo_url) as resp:
        details = resp.read().decode()
        details = json.loads(details)
        tasks = []
        done = 0
        for task in details:
            if task['completed']:
                done += 1
                tasks.append(task['title'])

        print(f"Employee name {name} is done with tasks({done}/{len(details)}):")
        for t in tasks:
            print(f"\t {t}")

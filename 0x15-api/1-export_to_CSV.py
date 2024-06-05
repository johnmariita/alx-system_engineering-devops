#!/usr/bin/python3
"""
Script that creates a csv file of a users
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
    filename = sys.argv[1] + '.csv'

    with open(filename, 'w') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for line in emps:
            if line['userId'] == int(sys.argv[1]):
                row = [sys.argv[1], users_json['username'],
                       line['completed'], line['title']]
                csv_writer.writerow(row)

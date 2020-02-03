#!/usr/bin/python3
""" using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import csv
import requests
import sys

if __name__ == "__main__":
    text = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    user_req = requests.get(text)
    to_do = requests.get(text + "/todos")
    list_to_do = to_do.json()
    user = user_req.json()
    list_done = []
    for element in list_to_do:
        if element.get('userId') == int(sys.argv[1]):
            tuple_final = (sys.argv[1], user.get('username'),
                           element.get('completed'), element.get('title'))
            list_done.append(tuple_final)

    with open(sys.argv[1]+'.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for el in list_done:
            writer.writerow((el[0], el[1], el[2], el[3]))

#!/usr/bin/python3
""" using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

text = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
user_req = requests.get(text)
to_do = requests.get(text + "/todos")
list_to_do = to_do.json()
user = user_req.json()
all_todo = 0
done = 0
list_done = []
for element in list_to_do:
    if element['userId'] == int(sys.argv[1]):
        all_todo += 1
        if element['completed'] == True:
            done += 1
            list_done.append(element['title'])

print("Employee {} is done with tasks({}/{}):".format(user['name'],
                                                      done, all_todo))
for title in list_done:
    print("\t {}".format(title))

#!/usr/bin/python3
""" using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import json
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

    list_dict = []
    for element in list_done:
        dict_list = {}
        dict_list["task"] = element[3]
        dict_list["completed"] = element[2]
        dict_list["username"] = element[1]
        list_dict.append(dict_list)
    dict_final = {sys.argv[1]: list_dict}

    with open(sys.argv[1]+'.json', 'w') as f:
        json.dump(dict_final, f)

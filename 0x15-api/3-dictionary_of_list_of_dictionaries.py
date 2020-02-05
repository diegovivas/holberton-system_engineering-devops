#!/usr/bin/python3
""" using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import json
import requests
import sys

if __name__ == "__main__":
    text = "https://jsonplaceholder.typicode.com/users/1"
    user_req = requests.get(text)
    to_do = requests.get(text + "/todos")
    list_to_do = to_do.json()
    user = user_req.json()
    list_done = []
    for element in list_to_do:
            tuple_final = (element.get('userId'), user.get('username'),
                           element.get('completed'), element.get('title'))
            list_done.append(tuple_final)
    dict_final = {}
    cont = 1
    while (cont <= 10):
        list_dict = []
        for element in list_done:
            if element[0] == cont:
                dict_list = {}
                dict_list["task"] = element[3]
                dict_list["completed"] = element[2]
                dict_list["username"] = element[1]
                list_dict.append(dict_list)
        dict_final[str(cont)] = list_dict
        cont += 1

    with open('todo_all_employees.json', 'w') as f:
        json.dump(dict_final, f)

#!/usr/bin/python3
"""
using the reddit api
"""
import requests


def top_ten(subreddit):
    """ print the first 10 hot post
    for a selected subreddit """
    requ = requests.get(
        "https://api.reddit.com/r/{}/hot".format(subreddit),
        headers={"User-Agent": "cualquiera"},
        params={'limit': '10'})
    try:
        flag = True
        for element in requ.json().get('data').get('children'):
            flag = False
            print(element.get('data').get('title'))
        if flag is True:
            print("None")
    except:
        print("None")

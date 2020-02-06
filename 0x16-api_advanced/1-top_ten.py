#!/usr/bin/python3
"""
using the reddit api
"""
import requests


def top_ten(subreddit):
    """ return the first 10 hot post
    for a selected subreddit """
    requ = requests.get(
        "https://api.reddit.com/r/{}/hot".format(subreddit),
        headers={"User-Agent": "cualquiera"},
        params={'limit': 10})

    if requ.status_code == 200:
        for element in requ.json().get('data').get('children'):
                print(element.get('data').get('title'))
    else:
        return 0
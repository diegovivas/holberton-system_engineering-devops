#!/usr/bin/python3
"""
using the reddit api
"""
import requests


def recurse(subreddit, hot_list=[]):
    """return a list of hot post
    for a selected subreddit """
    if len(hot_list) == 0:
        requ = requests.get(
            "https://api.reddit.com/r/{}/hot".format(subreddit),
            headers={"User-Agent": "cualquiera"})
    else:
        idx = len(hot_list) - 1
        requ = requests.get(
            "https://api.reddit.com/r/{}/hot".format(subreddit),
            headers={"User-Agent": "cualquiera"},
            params={'after': hot_list[idx]})
        del hot_list[idx]

    if requ.status_code != 200:
        return(None)

    request = requ.json().get('data').get('children')

    for element in request:
        hot_list.append(element.get('data').get('title'))
    sig = requ.json().get('data').get('after')
    if sig is not None:
        hot_list.append(sig)
        return recurse(subreddit, hot_list)
    else:
        return hot_list

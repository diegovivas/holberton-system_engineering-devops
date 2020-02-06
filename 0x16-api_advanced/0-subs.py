#!/usr/bin/python3
"""
using the reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """ return the number of subscribers
    for a selected subreddit """
    requ = requests.get(
        "https://api.reddit.com/r/{}/about".format(subreddit),
        headers={"User-Agent": "cualquiera"})
    if requ.status_code == 200:
        return requ.json().get('data').get('subscribers')
    else:
        return 0

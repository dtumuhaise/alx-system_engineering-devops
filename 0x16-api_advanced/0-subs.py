#!/usr/bin/python3
""" function that queries the reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """ function that queries Redit API and
    returns the number of subs of given subredit"""

    endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(endpoint)
    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        subs = data['data']['subscribers']
        return subs

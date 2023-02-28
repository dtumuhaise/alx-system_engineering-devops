#!/usr/bin/python3
""" recursive function """


import requests


def recurse(subreddit, hot_list=[]):
    """ recursive function that queries
    the Reddit API and returns a list
    containing the titles of all hot
    articles for a given subreddit."""

    endpoint = 'https://www.reddit.com/r/{}/hot.json?limit=10'\
        .format(subreddit)
    response = requests.get(endpoint)
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        return hot_list

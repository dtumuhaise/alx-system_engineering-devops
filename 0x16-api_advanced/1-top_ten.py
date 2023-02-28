#!/usr/bin/python3
""" writing a function """


import requests


def top_ten(subreddit):
    """ function that queries the Reddit
    API and prints the titles of the
    first 10 hot posts listed for a
    given subreddit."""

    endpoint = 'https://www.reddit.com/r/{}/hot.json?limit=10'\
        .format(subreddit)
    response = requests.get(endpoint)

    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])

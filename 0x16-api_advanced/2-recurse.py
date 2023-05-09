#!/usr/bin/python3
""" recursive function that queries
the Reddit API and returns a list
containing the titles of all
hot articles for a given  """

import requests


def recurse(subreddit, hot_list=[]):
    """ defining the function """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list)

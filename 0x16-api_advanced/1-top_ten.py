#!/usr/bin/python3
"""
 function that queries the Reddit API and
 prints the titles of the first 10 hot
 posts listed for a given subreddit.
 """

import requests


def top_ten(subreddit):
    """ defining the function """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print('None')
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])

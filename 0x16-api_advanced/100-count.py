#!/usr/bin/python3
""" recursive function that queries the Reddit API"""

import requests
import re

def count_words(subreddit, word_list, after=None, titles=''):
    """ function that queries the Reddit API,"""
    
    endpoint = 'https://www.reddit.com/r/{}/hot.json?limit=100'\
        .format(subreddit)

    headers = {'User-Agent': 'My-User-Agent'}
    params = {'after': after}
    response = requests.get(endpoint, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            titles += post['data']['title'] + ' '
        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, titles)
        else:
            word_dict = {}
            for word in set(word_list):
                word_dict[word] = 0
            for title in titles.split('\n'):
                title = title.lower()
                for word in set(word_list):
                    matches = re.findall(r'\b{}\b'.format(word.lower()), title)
                    word_dict[word] += len(matches)
            for key, value in sorted(word_dict.items(),
                                     key=lambda item: (-item[1], item[0])):
                if value != 0:
                    print('{}: {}'.format(key.lower(), value))

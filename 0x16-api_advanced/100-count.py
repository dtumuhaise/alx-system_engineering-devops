#!/usr/bin/python3
""" recursive function that queries the
Reddit API, parses the title of all
hot articles, and prints a sorted count
of given keywords (case-insensitive,
delimited by spaces.
"""

import requests


def count_words(subreddit, word_list, after=None, word_dic={}):
    """ defining the function """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                if word.lower() in title:
                    if word not in word_dic.keys():
                        word_dic[word] = 1
                    else:
                        word_dic[word] += 1
        after = data['data']['after']
        if after is None:
            if len(word_dic) == 0:
                return
            for key, value in sorted(word_dic.items(),
                                     key=lambda x: (-x[1], x[0])):
                print("{}: {}".format(key, value))
            return
        return count_words(subreddit, word_list, after, word_dic)

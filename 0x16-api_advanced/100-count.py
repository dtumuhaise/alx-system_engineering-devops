#!/usr/bin/python3

"""recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)"""

import requests


def count_words(subreddit, word_list, after=None, hot_list=[]):
    """ function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit."""

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
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, hot_list)
        else:
            word_dict = {}
            for word in word_list:
                word_dict[word] = 0
            for title in hot_list:
                words = title.split()
                for word in words:
                    word = word.lower()
                    if word in word_dict:
                        word_dict[word] += 1
            for key, value in sorted(word_dict.items(),
                                     key=lambda item: item[1],
                                     reverse=True):
                if value != 0:
                    print('{}: {}'.format(key, value))

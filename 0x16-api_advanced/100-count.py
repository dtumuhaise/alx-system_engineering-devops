#!/usr/bin/python3
""" recursive function that queries the
Reddit API, parses the title of all
hot articles, and prints a sorted count
of given keywords (case-insensitive,
delimited by spaces.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """ defining the function """
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'Mozilla/5.0'}

    if after:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']

        for article in articles:
            title = article['data']['title']
            for word in word_list:
                if word.lower() in title.lower().split():
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                print("{}: {}".format(word, count))

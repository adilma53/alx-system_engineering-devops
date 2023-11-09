#!/usr/bin/python3
""" parses titles of hot articles """

import requests
import sys
after = None
count = []


def count_words(subreddit, word_list):
    """ parse hot articles """
    global after
    global count
    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

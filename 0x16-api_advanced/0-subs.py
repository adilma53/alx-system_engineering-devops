#!/usr/bin/python3
""" get subscribers of reddit api """

import requests


def number_of_subscribers(subreddit):
    baseUrl = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Alx'}

    res = requests.get(baseUrl, headers=headers)
    if res.status_code == 200:
        resData = res.json()
        return resData['data']['subscribers']

    return 0

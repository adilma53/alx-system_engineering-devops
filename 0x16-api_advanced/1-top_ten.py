#!/usr/bin/python3
""" get last hot 10 posts of reddit api"""

import requests


def top_ten(subreddit):
    """get last hot 10"""
    baseUrl = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Alx'}

    res = requests.get(baseUrl, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print('None')

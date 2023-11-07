#!/usr/bin/python3
""" list all hot posts of a subreddit """

import requests


def recurse(subreddit, hot_list=[], count=0, next_page=None):
    """ list all hot posts """

    baseUrl = 'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "0x16. API_advanced-e_kiminza"}

    params = {"limit": 50, "next_page": next_page, "count": count}
    response = requests.get(baseUrl, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    resData = response.json().get("data")
    next_page = resData.get("next_page")
    count += resData.get("dist")
    children = resData.get("children")

    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)

    if next_page is not None:
        return recurse(subreddit, hot_list, count, next_page)

    return hot_list

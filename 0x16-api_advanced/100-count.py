#!/usr/bin/python3
""" parses titles of hot articles """

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """get words of hot posts"""
    headers = {"User-agent": "Mozilla/5.0"}
    posts = requests.get(f"http://www.reddit.com/r/{subreddit}/
                            hot.json?after={after}", headers=headers)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()["data"]
        aft = posts["after"]
        posts = posts["children"]
        for post in posts:
            title = post["data"]["title"].lower()
            for word in title.split(" "):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print(f"{key}: {value}")
    else:
        return

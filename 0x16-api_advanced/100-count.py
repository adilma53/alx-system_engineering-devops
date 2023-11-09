#!/usr/bin/python3
""" parses titles of hot articles """

from requests import get
from sys import argv

subreddit_titles = []
after = None


def count_all(subreddit_titles, word_list):
    """ parses hot articles """

    count_dict = {word.lower(): 0 for word in word_list}
    for title in subreddit_titles:
        words = title.split(' ')
        for word in words:
            if count_dict.get(word) is not None:
                count_dict[word] += 1

    for key in sorted(count_dict, key=count_dict.get, reverse=True):
        if count_dict.get(key):
            for thing in word_list:
                if key == thing.lower():
                    print("{}: {}".format(thing, count_dict[key]))


def count_words(subreddit, word_list):
    global subreddit_titles
    global after
    """subs"""
    headers = {'User-Agent': 'Dan Kazam'}
    if after:
        response = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after), headers=headers).json().get('data')
    else:
        response = get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=headers).json().get('data')
    subreddit_titles += [dic.get('data').get('title').lower()
                         for dic in response.get('children')]
    after = response.get('after')
    if after:
        return count_words(subreddit, word_list)
    return count_all(subreddit_titles, word_list)


if __name__ == "__main__":
    count_words(argv[1], argv[2].split(' '))

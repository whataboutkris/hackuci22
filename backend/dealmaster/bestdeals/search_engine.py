from urllib.parse import urlparse

from googlesearch import search
from .key_dics import car, book_genres, laptop, shoes


saving_keys = ['best price', 'best deal', 'sales']

categories = {'books': book_genres, 'car': car, 'shoes': shoes, 'laptop': laptop}


def key_generator(key_words):
    key_phrases = []

    item = key_words[0: (key_words.find(' '))]
    print(item)
    print(type(item))

    if item == 'car':
        item_list = car[key_words[(key_words.find(' ') + 1):]]

        print(key_words[(key_words.find(' ') + 1):])
        print('\n')
        print(item_list, '\n')

        for idx, model in enumerate(item_list):

            for saving_key in saving_keys:
                key_phrase = key_words + ' ' + model + ' ' + saving_key
                key_phrases.append(key_phrase)

    else:
        item_list = categories[item]

        print(item_list)

        for item in item_list:

            for saving_key in saving_keys:
                key_phrase = key_words + ' ' + item + ' ' + saving_key
                key_phrases.append(key_phrase)

    return key_phrases


"""
    Description: look for top 10 different websites which sell the specific item in query
    Parameters: query is a string describing the item
    Return: a dictionary, key is the homepage of that website, value is the url that user wants to see
"""


def search_best_deal(query):
    links = dict()
    modified_query = query + ' sales'
    for i in search(modified_query, tld="co.in", num=20, pause=2):
        url = urlparse(i)
        homepage = url.netloc
        # print(type(i))
        # print(type(homepage))

        if homepage not in links:
            links[homepage] = i

        if len(links) >= 10:
            break

    return links

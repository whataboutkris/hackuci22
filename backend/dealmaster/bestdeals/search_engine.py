from urllib.parse import urlparse

from googlesearch import search
from . import key_dics


# categories = {'books': book_genres, 'car': car, 'shoes': shoes, 'laptop': laptop}


def key_generator(key_words):
    key_phrases = []

    item = key_words[0: (key_words.find(' '))]
    print(item)
    print(type(item))

    if item == 'car':
        item_list = key_dics.car[key_words[(key_words.find(' ') + 1):]]

        print(key_words[(key_words.find(' ') + 1):])
        print('\n')
        print(item_list, '\n')

        for model in item_list[item]:
            key_phrase = key_words + ' ' + model + ' sales'
            key_phrases.append(key_phrase)

    else:
        item_list = []
        if item == 'books':
            item_list = key_dics.book_genres
        elif item == 'shoes':
            item_list = key_dics.accessories
        elif item == 'laptop':
            item_list = key_dics.laptop

        print(item_list)

        for item in item_list:
            key_phrase = key_words + ' ' + item + ' sales'
            key_phrases.append(key_phrase)

    return key_phrases


"""
    Description: look for top 10 different websites which sell the specific item in query
    Parameters: query is a string describing the item
    Return: a dictionary, key is the homepage of that website, value is the url that user wants to see
"""


def search_best_deal(query):
    links = dict()
    for i in search(query, tld="co.in", num=20, pause=2):
        url = urlparse(i)
        homepage = url.netloc
        # print(type(i))
        # print(type(homepage))

        if homepage not in links:
            links[homepage] = i

        if len(links) >= 10:
            break

    return links


# test1 = 'car toyota'
# test2 = 'books'
# test3 = 'nothing'
#
#
# result1 = key_generator(test1)
# result_search = search_best_deal('car toyota corolla best price')
# result3 = search_best_deal(key_generator(test1))
#
# print('Test 1 -------------')
# print(result1, '\n\n')
# print('Test 2 -------------')
# print(result_search, '\n\n')
# print('Test 3 -------------')
# print(result3, '\n\n')
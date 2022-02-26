from googlesearch import search

query = 'hp laptop'

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)


def search_request(request):
    url_list = []
    for j in search(request, tld="co.in", num=10, stop=10, pause=2):
        url_list.append(j)

    return url_list

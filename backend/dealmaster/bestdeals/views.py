from django.shortcuts import render
from . import search_engine, key_dics


# Create your views here.
def home_view(request):
    return render(request, 'main.html')


def about_view(request):
    return render(request, 'about.html')


def search_results(request):
    if request.GET.get('search_query'):
        results = search_engine.search_best_deal(request.GET.get('search_query'))
        context = {'results': results}
        return render(request, 'search-results.html', context)
    else:
        return render(request, 'main.html')


def cars_view(request):
    context = {'cars': key_dics.car}
    return render(request, 'cars.html', context)


def laptops_view(request):
    context = {'laptops': key_dics.laptop}
    return render(request, 'laptops.html', context)


def accessories_view(request):
    context = {'accessories': key_dics.accessories}
    return render(request, 'accessories.html', context)


def books_view(request):
    context = {'books': key_dics.book_genres}
    return render(request, 'books.html', context)


def bestdeals_view(request):
    context = {}
    return render(request, 'bestdeals.html', context)
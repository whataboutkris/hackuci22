from django.shortcuts import render
from . import search_engine


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


def laptop_view(request):
    return render(request, 'laptops.html')

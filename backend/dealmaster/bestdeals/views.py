from django.shortcuts import render
from . import search_engine


# Create your views here.
def home_view(request):
    return render(request, 'main.html')


def about_view(request):
    return render(request, 'about.html')


def search_results(request):
    return render(request, 'search.html')

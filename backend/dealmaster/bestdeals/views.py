from django.shortcuts import render
from . import search_engine


# Create your views here.
def home_view(request):

    return render(request, 'main.html')


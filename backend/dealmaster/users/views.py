from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse('Home Page in users')

def room(request):
    return HttpResponse("Room users")

def loginPage(request):
    return render(request, 'login.html')
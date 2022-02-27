from django.urls import path

from . import views

urlpatterns = [
    #path('users/register', views.register, name="home"),
    path('users/login', views.loginPage, name='login'),
]
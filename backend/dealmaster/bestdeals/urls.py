from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('home/', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('search/', views.search_results, name="search")

]
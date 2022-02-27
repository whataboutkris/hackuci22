from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('', views.home_view, name="home"),
    path('home/', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('search/', views.search_results, name="search"),
    path('bestdeals/', views.bestdeals_view, name="bestdeals"),

    # Sub pages for buttons
    path('laptop/', views.laptop_view, name="laptops"),
    path('car/', views.laptop_view, name="cars"),
    path('accessories/', views.laptop_view, name="accessories"),
    path('books/', views.laptop_view, name="books"),
]
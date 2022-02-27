from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('about/', views.about_view, name="about"),
    path('search-results/', views.search_results, name="search")

    # add urls

]
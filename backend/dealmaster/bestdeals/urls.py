from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
#<<<<<<< HEAD
# =======
    path('about/', views.about_view, name="about"),
    path('search-results/', views.search_results, name="search")

    # add urls

# >>>>>>> 7c1f65ef15906d62b506127bb973011d503d81f2
]
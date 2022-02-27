from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home_view, name="home_view"),
#<<<<<<< HEAD
# =======
=======
    path('', views.home_view, name="home"),
    path('home/', views.home_view, name="home"),
>>>>>>> a48bce78bceb97a458f0690989a68c98abc5d73e
    path('about/', views.about_view, name="about"),
    path('search/', views.search_results, name="search")

<<<<<<< HEAD
    # add urls

# >>>>>>> 7c1f65ef15906d62b506127bb973011d503d81f2
=======
>>>>>>> a48bce78bceb97a458f0690989a68c98abc5d73e
]
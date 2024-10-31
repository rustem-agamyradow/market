from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('search',views.search, name='search.html'),
    path('list',views.list, name='list.html'),
    path('haryt_profil',views.haryt_profil, name='haryt_profil.html'),
    
]
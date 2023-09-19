from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register, name="register"),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name= 'logout'),
    path('movies', views.movies, name= 'movies'),
    path('songs', views.songs, name= 'songs'),
    path('speeches', views.speeches, name= 'speeches'),
    path('gallery', views.gallery, name= 'gallery'),
    path('back', views.back, name= 'back'),
]
from importlib.resources import path
from pathlib import Path
from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/', views.tweet, name='tweet'),
    path('follow/', views.follow, name='follow'),
    path('followback/', views.followback, name='followback'),
]

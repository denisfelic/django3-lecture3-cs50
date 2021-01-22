from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('greet/<str:name>', views.greeting, name='greet'),
    path('home', views.home, name='home')
]

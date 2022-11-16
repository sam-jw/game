from . import  views
from django.urls import path

urlpatterns = [
    path('', views.startgame,name="start"),
    path('level/', views.levelgame,name="level"),
    path('game/', views.game,name='game'),
    path('cotegary/',views.category,name="category")
]
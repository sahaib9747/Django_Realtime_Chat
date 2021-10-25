from os import name
from django.urls import path 

from . import views 

urlpatterns = [
    path('login/', views.login, name="login"),
    path('send', views.send, name='send'),
    path('getmsg/<str:room>/', views.get_messages, name='get messages'),
    path('auth/', views.auth, name='auth'),
    path('chat/<str:room>/', views.chat, name='path'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('check_room', views.check_room, name='check_room'),
    path('send', views.send, name='send'),
    path('get_messages/<str:room_name>/',
         views.get_messages, name='get_messages'),
]

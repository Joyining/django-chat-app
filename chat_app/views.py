from django.shortcuts import render, redirect
from .models import Room

# Create your views here.


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'room.html')


def check_room(request):
    room_name = request.POST['room_name']
    user_name = request.POST['user_name']

    if not Room.objects.filter(name=room_name).exists():
        new_room = Room.objects.create(name=room_name)
        new_room.save()
    return redirect('/'+room_name+'/?user_name='+user_name)

from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    user_name = request.GET['user_name']
    room = Room.objects.get(name=room_name)
    context = {
        'room': room,
        'user_name': user_name
    }
    return render(request, 'room.html', context)


def check_room(request):
    room_name = request.POST['room_name']
    user_name = request.POST['user_name']

    if not Room.objects.filter(name=room_name).exists():
        new_room = Room.objects.create(name=room_name)
        new_room.save()
    return redirect('/'+room_name+'/?user_name='+user_name)


def send(request):
    message_value = request.POST['message_value']
    user_name = request.POST['user_name']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(
        value=message_value, user_name=user_name, room_id=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully!')


def get_messages(request, room_name):
    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room_id=room.id)
    return JsonResponse({"messages": list(messages.values())})

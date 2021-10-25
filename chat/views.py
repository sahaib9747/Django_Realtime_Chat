from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json

from .models import Room, Message

# Create your views here.
def login(request):
    status = request.GET.get('status')
    if not status:
        status = ''
    return render(request, 'index.html', {'status': status})


def chat(request, room):
    msg = Message.objects.filter(room=room)
    context = {
        "messages": False,
        "username": request.GET['username'],
        "room": room
    }
    if msg.exists():
        context["messages"] = msg

    return render(request, 'room.html', context)

def auth(request):
    room_name = request.POST['room-name']
    user_name = request.POST['user-name']
    password = request.POST['password']

    room = Room.objects.all().filter(name=room_name)

    if room.exists():
        room_info = room.get(name=room_name)
        if password == room_info.password:
            return redirect(f"/chat/{room_info.name}/?username={user_name}")
        else:
            return redirect('/login/?status=Check your credentials!! login Failed.')
    else:
        new = Room.objects.create(name=room_name, password=password)
        new.save()
        return redirect(f"chat/{room_name}/?username={user_name}")

def send(request):
    print(request.body)
    data = request.body.decode('utf-8')
    data = json.loads(data)

    new_message = Message.objects.create(user=data['username'], message=data['message'], room=data['room'])
    new_message.save()

    return HttpResponse('Message Saved!')

def get_messages(request,room):
    print(room)
    messages = Message.objects.all().filter(room=room)

    return JsonResponse({'messages': list(messages.values())})


from django.shortcuts import render
from .models import Room
# from django.http import HttpResponse


# rooms = [
#     Room(101, 'standard, street view', '1 king', True, False, True),
#     Room(204, 'standard, courtyard view', '2 queens', False, False, True),
#     Room(209, 'suite, street view', '1 king', False, True, False),
# ]


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/index.html', {'rooms': rooms})


def rooms_details(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'rooms/details.html', {'room': room})

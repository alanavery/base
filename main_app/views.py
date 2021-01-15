from django.shortcuts import render
# from django.http import HttpResponse


class Room:
    def __init__(self, number, room_type, beds, accessible, occupied, clean):
        self.number = number
        self.room_type = room_type
        self.beds = beds
        self.accessible = accessible
        self.occupied = occupied
        self.clean = clean


rooms = [
    Room(101, 'standard, street view', '1 king', True, False, True),
    Room(204, 'standard, courtyard view', '2 queens', False, False, True),
    Room(209, 'suite, street view', '1 king', False, True, False),
]


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    return render(request, 'rooms/index.html', {'rooms': rooms})

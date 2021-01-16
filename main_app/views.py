from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Room

# Create form views


class RoomCreate(CreateView):
    model = Room
    fields = '__all__'
    success_url = '/rooms'


class RoomUpdate(UpdateView):
    model = Room
    fields = ['beds', 'occupied', 'spotless']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(f'/rooms/{str(self.object.pk)}')


class RoomDelete(DeleteView):
    model = Room
    success_url = '/rooms'

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

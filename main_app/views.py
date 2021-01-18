from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Booking

# Create form views


class BookingCreate(CreateView):
    model = Booking
    fields = '__all__'
    success_url = '/bookings'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/bookings')


class BookingUpdate(UpdateView):
    model = Booking
    fields = ['check_in_date', 'check_out_date', 'total_guests']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(f'/bookings/{str(self.object.pk)}')


class BookingDelete(DeleteView):
    model = Booking
    success_url = '/bookings'

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def profile(request, username):
    user = User.objects.get(username=username)
    bookings = Booking.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'bookings': bookings})


def bookings_index(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/index.html', {'bookings': bookings})


def bookings_details(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'bookings/details.html', {'booking': booking})

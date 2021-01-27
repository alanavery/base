from django.db.models import Q, Count
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Guest, GuestId, Room, Booking
from .forms import AvailabilityForm, CreateBookingForm, GuestForm, SignupForm, LoginForm


def index(request):
    form = AvailabilityForm(label_suffix='')
    return render(request, 'index.html', {'form': form})


def signup(request):
    # /signup (POST)
    if request.method == 'POST':
        user_form = SignupForm(request.POST, label_suffix='')
        guest_form = GuestForm(request.POST, label_suffix='')
        if user_form.is_valid() and guest_form.is_valid:
            user = user_form.save()
            guest = guest_form.save()
            guest_id = GuestId(
                user=user,
                guest=guest
            )
            guest_id.save()
            login(request, user)
            return HttpResponseRedirect('/profile')

    # /signup (GET)
    else:
        user_form = SignupForm(request.POST, label_suffix='')
        guest_form = GuestForm(request.POST, label_suffix='')
        return render(request, 'signup.html', {
            'user_form': user_form,
            'guest_form': guest_form
        })


def login_view(request):
    # /login (POST)
    if request.method == 'POST':
        form = LoginForm(request, request.POST, label_suffix='')
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/profile')
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')

    # /login (GET)
    else:
        form = LoginForm(label_suffix='')
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def profile(request):
    user = request.user
    guest = user.guestid.guest
    bookings = Booking.objects.filter(guest=guest)
    user_form = SignupForm(instance=user, label_suffix='')
    guest_form = GuestForm(instance=guest, label_suffix='')
    return render(request, 'profile.html', {
        'user': user,
        'guest': guest,
        'bookings': bookings,
        'user_form': user_form,
        'guest_form': guest_form
    })


def update_user(request):
    user = request.user
    form = SignupForm(request.POST, instance=user)
    if form.is_valid():
        user = form.save()
        return HttpResponseRedirect('/')


def update_guest(request):
    guest = request.user.guestid.guest
    form = GuestForm(request.POST, instance=guest)
    if form.is_valid():
        guest = form.save()
        return HttpResponseRedirect('/profile')


# Booking process ——————————————————————————————


def book(request):
    form = AvailabilityForm(label_suffix='')
    if not request.GET:
        return render(request, 'book/index.html', {'form': form})
    else:
        check_in_date = request.GET.get('check_in_date')
        check_out_date = request.GET.get('check_out_date')
        request.session['check_in_date'] = check_in_date
        request.session['check_out_date'] = check_out_date
        request.session['total_guests'] = request.GET.get('total_guests')
        available_rooms = Room.objects.exclude(
            Q(booking__check_in_date__range=(check_in_date, check_out_date))
        ).exclude(
            Q(booking__check_out_date__range=(check_in_date, check_out_date))
        )
        results = {}
        for room in available_rooms:
            if room.room_type in results.keys():
                if room.beds in results[room.room_type].keys():
                    results[room.room_type][room.beds].append(room)
                else:
                    results[room.room_type][room.beds] = [room]
            else:
                bed_types = {}
                bed_types[room.beds] = [room]
                results[room.room_type] = bed_types
        return render(request, 'book/index.html', {
            'form': form,
            'results': results
        })


def create_booking(request, room_number):
    room = Room.objects.get(number=room_number)

    # /book/:room_number (POST)
    if request.method == 'POST':
        if request.user.is_authenticated:
            guest = request.user.guestid.guest
            form = GuestForm(request.POST, instance=guest)
            if form.is_valid():
                guest = form.save()
            else:
                print('Unable to update guest details—invalid form.')
        else:
            form = GuestForm(request.POST)
            if form.is_valid():
                guest = form.save()
        booking = Booking(
            guest=guest,
            room=room,
            check_in_date=(request.session['check_in_date']),
            check_out_date=(request.session['check_out_date']),
            total_guests=(request.session['total_guests'])
        )
        booking.save()
        return HttpResponseRedirect(f'/book/confirmation/{booking.id}')

    # /book/:room_number (GET)
    else:
        if request.user.is_authenticated:
            guest = request.user.guestid.guest
            form = GuestForm(instance=guest)
        else:
            form = GuestForm(label_suffix='')
        return render(request, 'book/create_booking.html', {
            'room': room,
            'form': form
        })


def book_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)

    # /book/confirmation/:booking_id (POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            guest_id = GuestId(
                user=user,
                guest=booking.guest
            )
            guest_id.save()
            login(request, user)
            return HttpResponseRedirect('/profile')

    # /book/confirmation/:booking_id (GET)
    else:
        form = SignupForm(label_suffix='')
        return render(request, 'book/confirmation.html', {'booking': booking, 'form': form})

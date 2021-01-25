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
from .forms import AvailabilityForm, CreateBookingForm, GuestCreationForm

# Generic views ——————————————————————————————


class BookingUpdate(UpdateView):
    model = Booking
    fields = ['check_in_date', 'check_out_date', 'total_guests']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(f'/bookings/{str(self.object.pk)}')


@method_decorator(login_required, name='dispatch')
class BookingDelete(DeleteView):
    model = Booking
    success_url = '/bookings'

# Create your views here.


def index(request):
    form = AvailabilityForm()
    return render(request, 'index.html', {'form': form})


def book(request):
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
    return render(request, 'book/index.html', {'results': results})


def create_booking(request, room_number):
    if request.method == 'POST':
        form = GuestCreationForm(request.POST)
        if form.is_valid():
            guest = form.save()
            room = Room.objects.get(number=room_number)
            booking = Booking(
                guest=guest,
                room=room,
                check_in_date=(request.session['check_in_date']),
                check_out_date=(request.session['check_out_date']),
                total_guests=(request.session['total_guests'])
            )
            booking.save()
            return HttpResponseRedirect(f'/book/confirmation/{booking.id}')
    else:
        if request.user.is_authenticated:
            guest = request.user.guestid.guest
            form = GuestCreationForm({
                'first_name': guest.first_name,
                'last_name': guest.last_name,
                'email': guest.email,
                'phone': guest.phone,
                'street': guest.street,
                'city': guest.city,
                'state': guest.state,
                'zip_code': guest.zip_code,
                'country': guest.country
            })
        else:
            form = GuestCreationForm()
        return render(request, 'book/create_booking.html', {'form': form})


def book_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
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
    else:
        form = UserCreationForm()
        return render(request, 'book/confirmation.html', {'booking': booking, 'form': form})


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        guest_form = GuestCreationForm(request.POST)
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
    else:
        user_form = UserCreationForm(request.POST)
        guest_form = GuestCreationForm(request.POST)
        return render(request, 'signup.html', {
            'user_form': user_form,
            'guest_form': guest_form
        })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
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
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def profile(request):
    user = request.user
    guest = user.guestid.guest
    bookings = Booking.objects.filter(guest=guest)
    return render(request, 'profile.html', {
        'user': user,
        'guest': guest,
        'bookings': bookings
    })


def bookings_index(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/index.html', {'bookings': bookings})


def bookings_details(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'bookings/details.html', {'booking': booking})

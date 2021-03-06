from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Guest(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    credit_card = models.CharField(max_length=16)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=2)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return str(self.id)


class GuestId(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)


class Room(models.Model):
    number = models.PositiveIntegerField()
    room_type = models.CharField(max_length=150)
    beds = models.CharField(max_length=150)
    accessible = models.BooleanField()
    occupied = models.BooleanField()
    spotless = models.BooleanField()

    def __str__(self):
        return str(self.number)


class Booking(models.Model):
    TOTAL_GUESTS_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4)]
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    check_in_date = models.DateField()
    check_in_time = models.TimeField(default='15:00:00')
    check_out_date = models.DateField()
    check_out_time = models.TimeField(default='12:00:00')
    total_guests = models.PositiveIntegerField(
        choices=TOTAL_GUESTS_CHOICES, default=1)
    rate = models.FloatField(default=100)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

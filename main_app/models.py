from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    confirmation = models.PositiveIntegerField()
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    total_guests = models.PositiveIntegerField()
    guest_first_name = models.CharField(max_length=100)
    guest_last_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=100)
    guest_street = models.CharField(max_length=100)
    guest_city = models.CharField(max_length=100)
    guest_state = models.CharField(max_length=100)
    guest_zip = models.CharField(max_length=100)
    guest_country = models.CharField(max_length=100)
    rate = models.FloatField()
    paid = models.BooleanField()
    notes = models.TextField()

    def __str__(self):
        return str(self.confirmation)


class Room(models.Model):
    number = models.PositiveIntegerField()
    room_type = models.CharField(max_length=100)
    beds = models.CharField(max_length=100)
    accessible = models.BooleanField()
    occupied = models.BooleanField()
    spotless = models.BooleanField()

    def __str__(self):
        return str(self.number)

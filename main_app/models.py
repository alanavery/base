from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    online_account = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Room(models.Model):
    number = models.PositiveIntegerField(unique=True)
    room_type = models.CharField(max_length=150)
    beds = models.CharField(max_length=150)
    accessible = models.BooleanField()
    occupied = models.BooleanField()
    spotless = models.BooleanField()

    def __str__(self):
        return str(self.number)


class Booking(models.Model):
    confirmation = models.PositiveIntegerField(unique=True)
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    total_guests = models.PositiveIntegerField()
    rate = models.FloatField()
    paid = models.BooleanField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.confirmation)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class GuestProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_guest_profile(sender, instance, created, **kwargs):
    if created:
        GuestProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_guest_profile(sender, instance, **kwargs):
    instance.guestprofile.save()


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
    confirmation = models.PositiveIntegerField()
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    total_guests = models.PositiveIntegerField()
    rate = models.FloatField()
    paid = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.confirmation)

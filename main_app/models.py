from django.db import models

# Create your models here.


class Room(models.Model):
    number = models.PositiveIntegerField()
    room_type = models.CharField(max_length=100)
    beds = models.CharField(max_length=100)
    accessible = models.BooleanField()
    occupied = models.BooleanField()
    spotless = models.BooleanField()

    def __str__(self):
        return str(self.number)

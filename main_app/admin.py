from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import GuestProfile, Room, Booking


class GuestProfileInline(admin.StackedInline):
    model = GuestProfile
    can_delete = False
    verbose_name_plural = 'guest profile'


class UserAdmin(BaseUserAdmin):
    inlines = (GuestProfileInline,)


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Room)
admin.site.register(Booking)

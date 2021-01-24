from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Guest, GuestId, Room, Booking

class GuestIdInline(admin.StackedInline):
    model = GuestId
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (GuestIdInline,)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'room', 'check_in_date', 'check_out_date')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)

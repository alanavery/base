from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Room, Booking


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('phone', 'street', 'city', 'state', 'zip_code', 'country')
        }),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields = ('last_login', 'date_joined')


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Room)
admin.site.register(Booking)

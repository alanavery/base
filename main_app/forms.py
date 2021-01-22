from django import forms
from django.contrib.auth.models import User

from .models import GuestProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class GuestProfileForm(forms.ModelForm):
    class Meta:
        model = GuestProfile
        fields = ('phone', 'street', 'city', 'state', 'zip_code', 'country')

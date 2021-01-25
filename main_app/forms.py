from django import forms
from .models import Guest, Booking

class AvailabilityForm(forms.Form):
    check_in_date = forms.DateField(label='Check-In Date')
    check_out_date = forms.DateField(label='Check-Out Date')
    total_guests = forms.IntegerField()

    check_in_date.widget.attrs.update({'class': 'datepicker'})
    check_out_date.widget.attrs.update({'class': 'datepicker'})

class CreateGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
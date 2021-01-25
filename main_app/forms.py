from django.forms import ModelForm, DateInput, Select
from .models import Guest, Booking

class AvailabilityForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'total_guests']
        labels = {
            'check_in_date': 'Check-In Date',
            'check_out_date': 'Check-Out Date',
            'total_guests': 'Total Guests'
        }
        widgets = {
            'check_in_date': DateInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'YYYY-MM-DD'
            }),
            'check_out_date': DateInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'YYYY-MM-DD'
            }),
            'total_guests': Select(attrs={
                'class': 'form-select',
                'placeholder': '1'
            })
        }

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

class CreateBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
from django.forms import ModelForm, DateInput
from .models import Guest, Booking

class AvailabilityForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'total_guests']
        widgets = {
            'check_in_date': DateInput(attrs={'class': 'datepicker'}),
            'check_out_date': DateInput(attrs={'class': 'datepicker'})
        }

class GuestCreationForm(ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

class CreateBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
from django.forms import ModelForm, DateInput, Select, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Guest, Booking


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].label = 'Password Confirmation'


class AvailabilityForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'total_guests']
        labels = {
            'check_in_date': 'Check-In Date',
            'check_out_date': 'Check-Out Date',
            'total_guests': 'Number of Guests'
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
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'zip_code': 'Zip Code'
        }
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'John'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Smith'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'jsmith@email.com'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '5555555555'
            }),
            'street': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '123 Main St'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Chicago'
            }),
            'state': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'IL'
            }),
            'zip_code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '12345'
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'United States'
            })
        }


class CreateBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

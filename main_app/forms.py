from django import forms

class AvailabilityForm(forms.Form):
    check_in_date = forms.DateField(label='Check-In Date')
    check_out_date = forms.DateField(label='Check-Out Date')

    check_in_date.widget.attrs.update({'class': 'datepicker'})
    check_out_date.widget.attrs.update({'class': 'datepicker'})
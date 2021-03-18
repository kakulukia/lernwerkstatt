from django import forms
from django.core.exceptions import ValidationError

from bookings.models import Booking, TimeSlot


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    timeslot = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=TimeSlot.data.all(), label="Zeitraum")

    class Meta:
        model = Booking
        exclude = ['status']
        widgets = {
            'start': DateInput()
        }

    def clean_group_size(self):
        data = self.cleaned_data

        if data['group_size'] > 24:
            raise ValidationError('Wir haben leider nur Platz für Gruppen bis zu einer Größe von maximal 24 Personen.')

        return data['group_size']

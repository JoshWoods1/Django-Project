from django import forms

class BookingForm(forms.Form):
    tickets_booked = forms.IntegerField(label='Tickets Booked')

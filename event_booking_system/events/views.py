from django.shortcuts import render, redirect
from .models import Event, Booking
from .forms import BookingForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def book_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            tickets_booked = form.cleaned_data['tickets_booked']
            Booking.objects.create(event=event, user=request.user, tickets_booked=tickets_booked)
            return redirect('event_list')
    else:
        form = BookingForm()
    return render(request, 'events/book_event.html', {'event': event, 'form': form})

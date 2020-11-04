from django.shortcuts import render

# Create your views here.

def events (request):
    """ A view to return the events page """

    return render(request, 'events/events.html')

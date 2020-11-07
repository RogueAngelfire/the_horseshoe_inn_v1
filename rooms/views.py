from django.shortcuts import render
from .models import Room, Category

# Create your views here.

def rooms(request):
    """ A view to return the accomadation page """

    room = Room.objects.all()

    context = {
        'rooms': room,
    }

    return render(request, 'rooms/rooms.html', context)
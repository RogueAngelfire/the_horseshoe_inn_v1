from django.shortcuts import render, get_object_or_404
from .models import Room, Category

# Create your views here.

def rooms(request):
    """ A view to return the accomadation page """

    room = Room.objects.all()

    context = {
        'rooms': room,
    }

    return render(request, 'rooms/rooms.html', context)

def room_detail(request, room):
    """ A view to show individual room details """

    room = get_object_or_404(Room, pk=room_id)

    context = {
        'room': room,
    }

    return render(request, 'rooms/room_detail.html', context)
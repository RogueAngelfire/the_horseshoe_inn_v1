from django.shortcuts import render, get_object_or_404
from .models import Room, Category

# Create your views here.

def rooms(request):
    """ A view to return the all the accommadation page """

    rooms = Room.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            rooms = rooms.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'rooms': rooms,
        'current_categories': categories,
    }

    return render(request, 'rooms/rooms.html', context)

def room_detail(request, room_id):
    """ A view to show individual room details """

    room = get_object_or_404(Room, pk=room_id)

    context = {
        'room': room,
    }

    return render(request, 'rooms/room_detail.html', context)

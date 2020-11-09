from django.shortcuts import render, get_object_or_404
from .models import Room, Category

# Create your views here.

def rooms(request):
    """ A view to return the all the accomadation page """

    rooms = Room.objects.all()
    category = None
    print(f"REQUEST: {request.GET}")
    if request.GET:
        if 'category' in request.GET:
            print(f"categories in the request: {request.GET['category']}")
            categories = request.GET['category'].split(',')
            print(f"categories are: {categories}")
            rooms = rooms.filter(category__name__in=categories)
            print(f"rooms are: {rooms}")
            category = Category.objects.filter(name__in=categories)

    context = {
        'rooms': rooms,
    }

    return render(request, 'rooms/rooms.html', context)

def room_detail(request, room):
    """ A view to show individual room details """

    room = get_object_or_404(Category, Room, pk=room_id)

    context = {
        'room': room,
    }

    return render(request, 'rooms/room_detail.html', context)


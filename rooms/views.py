from django.shortcuts import render

# Create your views here.

def rooms(request):
    """ A view to return the accomadation page """

    return render(request, 'rooms/rooms.html')
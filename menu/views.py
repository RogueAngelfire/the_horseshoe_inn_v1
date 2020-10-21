from django.shortcuts import render

# Create your views here.

def menu(request):
    """ A view to return the menu page """

    return render(request, 'menu/menu.html')

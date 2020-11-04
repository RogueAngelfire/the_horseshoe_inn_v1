from django.shortcuts import render
from .models import Menu

# Create your views here.

def menu(request):
    """ A view to return the menu page """


    menu_items = Menu.objects.all()
    context = {
        'menu_items': menu_items,
    }
    return render(request, 'menu/menu.html', context)

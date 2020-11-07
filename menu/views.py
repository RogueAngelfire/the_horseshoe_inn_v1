from django.shortcuts import render
from .models import Menu, Category

# Create your views here.

def menu(request):
    """ A view to return the menu page """

    menu = Menu.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu.html', context)

from django.shortcuts import render
from .models import Menu, Category

# Create your views here.

def menu_items(request):
    """ A view to show all Menu items, including sorting - No search required at this stage of development """

def menu(request):
    """ A view to return the menu page """

    categories = Category.objects.all()

    menu = Menu.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu.html', context)

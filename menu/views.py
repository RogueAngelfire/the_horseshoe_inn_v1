from django.shortcuts import render, get_object_or_404
from .models import Menu, Category

# Create your views here.

def menu(request):
    """ A view to return the menu page """

    menu = Menu.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            menu = menu.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


    context = {
        'menu': menu,
        'current_categories': categories,
    }

    return render(request, 'menu/menu.html', context)

def menu_detail(request, menu_id):
    """ A view to show individual menu items """

    menu = get_object_or_404(Menu, pk=menu_id)

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu_detail.html', context)

from django.shortcuts import render
from .models import Menu, Category

# Create your views here.

def menu(request):
    """ A view to return the menu page """

    menu = Menu.objects.all()
    category = None
    if request.GET:
        if 'category' in request.GET:
            print(f"categories in the request: {request.GET['category']}")
            categories = request.GET['category'].split(',')
            print(f"categories are: {categories}")
            menu = menu.filter(category__name__in=categories)
            print(f"menu are: {menu}")
            category = Category.objects.filter(name__in=categories)


    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu.html', context)

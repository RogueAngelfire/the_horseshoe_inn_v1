from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Menu, Category

# Create your views here.

def menu(request):
    
    """ A view to return the menu page """

    menu = Menu.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:	
        if 'sort' in request.GET:	
            sortkey = request.GET['sort']	
            sort = sortkey	
            if sortkey == 'name':	
                sortkey = 'lower_name'	
                rooms = rooms.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:	
                direction = request.GET['direction']	
                if direction == 'desc':	
                    sortkey = f'-{sortkey}'	
            menu = menu.order_by(sortkey)

    if 'category' in request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            menu = menu.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    """ Search bar remove if you decide not to use one """

    if 'q' in request.GET:	
        query = request.GET['q']	
        if not query:	
            messages.error(request, "You didn't enter any search criteria!")	
            return redirect(reverse('menu'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)	
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'menu': menu,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'menu/menu.html', context)

def menu_detail(request, menu_id):
    """ A view to show individual menu items """

    menu = get_object_or_404(Menu, pk=menu_id)

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu_detail.html', context)

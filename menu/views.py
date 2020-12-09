from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Menu, Category
from .forms import MenuForm

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


@login_required
def add_menu(request):
    """ Add a Menu item to the Pub Menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only The Horseshoe Inn admin team can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save()
            messages.success(request, 'Menu Item Successfully Added!')
            return redirect(reverse('menu_detail', args=[menu.id]))
        else:
            messages.error(request, 'Failed to Add menu item. Please ensure the form is valid.')
    else:
        form = MenuForm()

    template = 'menu/add_menu.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_menu(request, menu_id):
    """ Edit a menu item for the pub """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only The Horseshoe Inn admin team can do that.')
        return redirect(reverse('home'))

    menu = get_object_or_404(Menu, pk=menu_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Menu item!')
            return redirect(reverse('menu_detail', args=[menu.id]))
        else:
            messages.error(request, 'Failed to update the Menu. Please ensure the form is valid.')
    else:
        form = MenuForm(instance=menu)
        messages.info(request, f'You are editing {menu.name}')

    template = 'menu/edit_menu.html'
    context = {
        'form': form,
        'menu': menu,
    }

    return render(request, template, context)


@login_required
def delete_menu(request, menu_id):
    """ Delete a item from the pub menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only The Horseshoe Inn admin team can do that.')
        return redirect(reverse('home'))

    menu = get_object_or_404(Menu, pk=menu_id)
    menu.delete()
    messages.success(request, 'Menu item deleted!')
    return redirect(reverse('menu'))

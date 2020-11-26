from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Room, Category

# Create your views here.

def rooms(request):

    """ A view to return the all the accommadation page """

    rooms = Room.objects.all()
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
            rooms = rooms.order_by(sortkey)

    if 'category' in request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            rooms = rooms.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    """ Search bar remove if you decide not to use one CURRENTLY INACTIVE client may change mind """

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('rooms'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'rooms': rooms,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'rooms/rooms.html', context)


def room_detail(request, room_id):
    """ A view to show individual room details """

    room = get_object_or_404(Room, pk=room_id)

    context = {
        'room': room,
    }

    return render(request, 'rooms/room_detail.html', context)

   # Below is experiment code to function the Datepicker(s)


def add_date(request, item_id):
    """ Add a booking """

    room = get_object_or_404(Room, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    add_date = request.POST.get('add_date')
    print(add_date)
    redirect_url = request.POST.get('redirect_url')

    if 'number_available' in request.POST:
        free = request.POST['number_available']
    datepicker = request.session.get('room_datepicker', {})
    if free:
        if item_id in list(datepicker.keys()):
            if free in datepicker[item_id]['items_by_free'].keys():
                datepicker[item_id]['items_by_free'][free] += quantity
                messages.success(request, f'Updated free {free.upper()} {room.name} quantity to {datepicker[item_id]["items_by_free"][free]}')
            else:
                datepicker[item_id]['items_by_free'][free] = quantity
                messages.success(request, f'Added free {free.upper()} {room.name} to datepicker')
        else:
            datepicker[item_id] = {'items_by_free': {free: quantity}}
            messages.success(request, f'Added free {free.upper()} {room.name} to book')
    else:
        if item_id in list(datepicker.keys()):
            datepicker[item_id] += quantity
            messages.success
            (request, f'Updated {room.name} quantity to {datepicker[item_id]}')
        else:
            book[item_id] = quantity
            messages.success(request, f'Added {room.name} to datepicker')

    request.session['datepicker'] = datepicker
    return redirect(redirect_url)


from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower


from .models import Room, Category
from .forms import RoomForm

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


@login_required
def add_room(request):
    """ Add a Room to the Pub """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only The Horseshoe Inn admin team can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save()
            messages.success(request, 'Room Successfully Added!')
            return redirect(reverse('room_detail', args=[room.id]))
        else:
            messages.error(
                request, 'Failed to Add Room. Please ensure the form is valid.')
    else:
        form = RoomForm()

    template = 'rooms/add_room.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_room(request, room_id):
    """ Edit a room for the pub """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only The Horseshoe Inn admin team can do that.')
        return redirect(reverse('home'))

    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Room!')
            return redirect(reverse('room_detail', args=[room.id]))
        else:
            messages.error(
                request, 'Failed to update the Room. Please ensure the form is valid.')
    else:
        form = RoomForm(instance=room)
        messages.info(request, f'You are editing {room.name}')

    template = 'rooms/edit_room.html'
    context = {
        'form': form,
        'room': room,
    }

    return render(request, template, context)


@login_required
def delete_room(request, room_id):
    """ Delete a room from the pub """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only The Horseshoe Inn admin team can do that.')
        return redirect(reverse('home'))

    room = get_object_or_404(Room, pk=room_id)
    room.delete()
    messages.success(request, 'Room deleted!')
    return redirect(reverse('rooms'))

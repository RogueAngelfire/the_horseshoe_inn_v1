from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from rooms.models import Room

# Create your views here.

def view_book(request):
    """ A view that renders the booking contents page """

    return render(request, 'book/book.html')


def add_to_book(request, item_id):
    """ Add a quantity of the specified rooms to the booking shopping bag """

    room = get_object_or_404(Room, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    date = request.POST.get('date')
    number_of_nights = int(request.POST.get('number_of_nights'))
    redirect_url = request.POST.get('redirect_url')
    book = request.session.get('book', {})
    if date:
        if item_id in list(book.keys()):
            if date in book[item_id] ['items_by_date'].keys():
                book[item_id]['items_by_date'][date]['number_guests'] += quantity
                book[item_id]['items_by_date'][date]['number_of_nights'] += add_to_book
                messages.success(request, f'booking for arrival on {date.upper()} for {room.name} is confirmed')
            else:
                book[item_id]['items_by_date'][date] = {}
                book[item_id]['items_by_date'][date]['number_guests'] = quantity
                book[item_id]['item_by_date'][date]['number_nights'] = number_of_nights
                messages.success(request, f'Date added for {date.upper()} {room.name} to your booking')
        else:
            book[item_id] = {'items_by_date': {date: {'number_guests': quantity, 'number_of_nights': number_of_nights}}}
            messages.success(request, f'Added a date {date.upper()} {room.name} to your booking')

    if item_id in list(book.keys()):
        book[item_id] += quantity
    else:
        book[item_id] = quantity

    request.session['book'] = book
    return redirect(redirect_url)

    if size:
        if item_id in list(book.keys()):
            if size in book[item_id]['items_by_size'].keys():
                book[item_id]['items_by_size'][size] += quantity
            else:
                book[item_id]['items_by_size'][size] = quantity
        else:
            book[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(book.keys()):
            book[item_id] += quantity
        else:
            book[item_id] = quantity

    request.session['book'] = book
    return redirect(redirect_url)

    if 'checkin_date' in request.POST:
        date = request.POST['checkin_date']

    book = request.session.get('book', {})


def adjust_booking(request, item_id):
    """ Adjust the guest quantity """

    room = get_object_or_404(Room, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'room_size' in request.POST:
        size = request.POST['room_size']
    book = request.session.get('book', {})

    if size:
        if quantity > 0:
            book[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated room {size.upper()}{room.name} quantity to {book[item_id]["items_by_size"][size]}')
        else:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
                messages.success(request, f'Removed Room {size.upper()} {room.name} from your booking')
    else:
        if quantity > 0:
            book[item_id] = quantity
            messages.success(request, f'Removed Room {room.name} from your booking')
        else:
            book.pop(item_id)
            messages.success(request, f'Removes {room.name} from your booking')

    request.session['book'] = book
    return redirect(reverse('view_book'))


def remove_from_booking(request, item_id):
    """Remove the item from the booking bag"""

    try:
        size = None
        if 'room_size' in request.POST:
            size = request.POST['room_size']
        book = request.session.get('book', {})

        if size:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
        else:
            book.pop(item_id)

        request.session['book'] = book
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

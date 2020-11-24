from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
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
    date = request.POST.get('add_date')
    number_of_nights = int(request.POST.get('number_of_nights'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'room_size' in request.POST:
        size = request.POST['room_size']
    book = request.session.get('book', {})

    # if date:
    #     print("date")
    if item_id in list(book.keys()):
        if date in book[item_id]['items_by_date'].keys():
            book[item_id]['items_by_date'][date]['number_guests'] += quantity
            book[item_id]['items_by_date'][date]['number_of_nights'] += number_of_nights
            messages.success(request, f'booking for arrival on {date.upper()} in {room.name} has been amended')
        else:
            book[item_id]['items_by_date'][date] = {}
            book[item_id]['items_by_date'][date]['number_guests'] = quantity
            book[item_id]['item_by_date'][date]['number_of_nights'] = number_of_nights
            messages.success(request, f'Date added for {date.upper()} {room.name} to your booking')
    else:
        book[item_id] = {'items_by_date': {date: {'number_guests': quantity, 'number_of_nights': number_of_nights}}}
        messages.success(request, f'Added a date {date.upper()} {room.name} to your booking')
        print(book)

    # if item_id in list(book.keys()):
    #     book[item_id] += quantity
    # else:
    #     book[item_id] = quantity
    #     messages.success(request, f'Added {room.name} to your booking')

    request.session['book'] = book
    return redirect(redirect_url)

    """ Remove certain sizes that has no purpose on completion after testing """

    if size:
        if item_id in list(book.keys()):
            if size in book[item_id]['items_by_size'].keys():
                book[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'REMOVE added size {room.name} to your to {book[item_id]["items_by_size"][size]}')
            else:
                book[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added {size.upper()} {room.name} to your booking')
        else:
            book[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'REMOVE added size {room.name} to your booking')
    else:
        if item_id in list(book.keys()):
            book[item_id] += quantity
            messages.success(request, f'Added size {room.name} to your booking {book[item_id]}')
        else:
            book[item_id] = quantity
            messages.success(request, f'Added {room.name} to your booking')

    request.session['book'] = book
    return redirect(redirect_url)

    if 'checkin_date' in request.POST:
        date = request.POST['checkin_date']
    book = request.session.get('book', {})


def adjust_booking(request, item_id):
    """ Adjust the booking by adding and subtacting guests quantity """

    room = get_object_or_404(Room, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'room_size' in request.POST:
        size = request.POST['room_size']
    book = request.session.get('book', {})

    if size:
        if quantity > 0:
            book[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated {size.upper()} {room.name} quantity to {book[item_id]["items_by_size"][size]}')
        else:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
            messages.success(request, f'Removed {size.upper()} {room.name} from your booking')
    else:
        if quantity > 0:
            book[item_id] = quantity
            messages.success(request, f'Updated {room.name} quantity to {book[item_id]}')
        else:
            book.pop(item_id)
            messages.success(request, f'Removed {room.name} from booking')

    request.session['book'] = book
    return redirect(reverse('view_book'))


def remove_from_booking(request, item_id):
    """Remove the item from the booking bag"""

    try:
        room = get_object_or_404(Room, pk=item_id)
        size = None
        if 'room_size' in request.POST:
            size = request.POST['room_size']
        book = request.session.get('book', {})

        if size:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
            messages.success(request, f'Removed {size.upper()} {room.name} from your booking')
        else:
            book.pop(item_id)
            messages.success(request, f'Removed {room.name} from your booking')

        request.session['book'] = book
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing booking: {e}')
        return HttpResponse(status=500)

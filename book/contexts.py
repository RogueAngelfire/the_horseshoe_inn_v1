from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from rooms.models import Room
<<<<<<< HEAD
import datetime
=======
>>>>>>> 2b4ae1d4a563dcada7f545abe09ef5c640b54957


def book_contents(request):

    book_items = []
    total = 0
    room_count = 0
    book = request.session.get('book', {})
<<<<<<< HEAD
    print(book)
    print(f"BOOK ITEMS: {book.items()}")

    for item_id, items_by_date, date, number_guests, quantity in book.items():
        room = get_object_or_404(Room, pk=item_id)
        total += quantity #* room.price
        room_count += quantity
        book_items.append({
            'item_id': item_id,
            'items_by_date': items_by_date,
            'date': date,
            'number_guests': number_guests,
=======

    for item_id, quantity in book.items():
        room = get_object_or_404(Room, pk=item_id)
        total += quantity * room.price
        room_count += quantity
        book_items.append({
            'item_id': item_id,
>>>>>>> 2b4ae1d4a563dcada7f545abe09ef5c640b54957
            'quantity': quantity,
            'room': room,
        })

    grand_total = total

    context = {
        'book_items': book_items,
        'total': total,
        'room_count': room_count,
        'grand_total': grand_total,
    }

    return context

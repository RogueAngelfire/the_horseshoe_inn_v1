from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from rooms.models import Room
import datetime


def book_contents(request):

    book_items = []
    total = 0
    room_count = 0
    book = request.session.get('book', {})
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

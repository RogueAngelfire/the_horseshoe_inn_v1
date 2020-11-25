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
    
    for item_id, booking_detail in book.items():
        room = get_object_or_404(Room, pk=item_id)
        item_by_date = booking_detail['item_by_date']
        number_of_nights = booking_detail['number_of_nights']
        number_guests = booking_detail['number_guests']
        total_room_price = number_of_nights * room.price
        book_items.append({
            'item_id': item_id,
            'items_by_date': items_by_date,
            'number_guests': number_guests,
        })

    grand_total = total

    context = {
        'book_items': book_items,
        'total_room_price': total_room_price,
        'room_count': room_count,
        'grand_total': grand_total,
    }

    return context

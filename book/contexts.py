from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from rooms.models import Room


def book_contents(request):

    book_items = []
    total_room_price = 0
    room_count = 0
    book = request.session.get('book', {})
    print(f"book is {book}")
    print(f"BOOK ITEMS: {book.items()}")

    for item_id, booking_detail in book.items():
        room = get_object_or_404(Room, pk=item_id)
        items_by_date = booking_detail['items_by_date']
        number_of_nights = booking_detail['number_of_nights']
        number_guests = booking_detail['number_guests']
        total_room_price += number_of_nights * room.price
        book_items.append({
            'item_id': item_id,
            'items_by_date': items_by_date,
            'number_of_nights': number_of_nights,
            'number_guests': number_guests,
        })

    grand_total = total

    context = {
        'book_items': book_items,
        'number_guests': number_guests,
        'number_of_nights': number_of_nights,
        'total_room_price': total_room_price,
        'grand_total': grand_total,
    }

    return context

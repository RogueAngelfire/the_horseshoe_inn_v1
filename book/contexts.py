from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from rooms.models import Room


def book_contents(request):

    book_items = []
    number_guests = 0
    number_of_nights = 0
    total_room_price = 0
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
            'room': room,
            'item_id': item_id,
            'items_by_date': items_by_date,
            'number_of_nights': number_of_nights,
            'number_guests': number_guests,
        })

    grand_total = total_room_price * number_of_nights

    context = {
        'book_items': book_items,
        'number_guests': number_guests,
        'number_of_nights': number_of_nights,
        'total_room_price': total_room_price,
        'grand_total': grand_total,
    }

    return context

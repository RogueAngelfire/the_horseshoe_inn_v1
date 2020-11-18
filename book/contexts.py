from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from rooms.models import Room


def book_contents(request):

    book_items = []
    total = 0
    room_count = 0
    book = request.session.get('book', {})

    for item_id, quantity in book.items():
        room = get_object_or_404(Room, pk=item_id)
        total += quantity * room.price
        room_count += quantity
        book_items.append({
            'item_id': item_id,
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

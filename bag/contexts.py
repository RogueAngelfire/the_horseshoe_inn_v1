from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from rooms.models import Room


def bag_contents(request):

    bag_items = []
    total = 0
    room_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        room = get_object_or_404(Room, pk=item_id)
        total += quantity * room.price
        room_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'room': room,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'room_count': room_count,
        'grand_total': grand_total,
    }

    return context

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Room

from .forms import OrderForm


def checkout(request):
    book = request.session.get('book', {})
    if not book:
        messages.error(request, "You have no bookings at the moment")
        return redirect(reverse('rooms'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


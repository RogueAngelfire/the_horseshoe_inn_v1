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
<<<<<<< HEAD
        'stripe_public_key': 'pk_test_51HqySkAWCoFdy1sCBt5Qitw6n1KfxzcPAWk0g0v8n4KFPAasMlT0PY5xeCeQ2Iz34f6jXIP2oBDxgW2E18Z1gsXW00Oh6gUfr0',
        'client_secret': 'test client_secret',
=======
>>>>>>> 2b4ae1d4a563dcada7f545abe09ef5c640b54957
    }

    return render(request, template, context)


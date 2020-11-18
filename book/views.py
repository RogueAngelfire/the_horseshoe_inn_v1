from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from rooms.models import Room

# Create your views here.

def view_book(request):
    """ A view that renders the booking contents page """

    return render(request, 'book/book.html')

def add_to_book(request, item_id):
    """ Add a quantity of the specified rooms to the booking shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    book = request.session.get('book', {})

    if item_id in list(book.keys()):
        book[item_id] += quantity
    else:
        book[item_id] = quantity

    request.session['book'] = book
    return redirect(redirect_url)

from django.shortcuts import render

# Create your views here.

def special_offers (request):
    """ A view to return the special offers page """

    return render(request, 'special_offers.html')

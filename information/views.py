from django.shortcuts import render

# Create your views here.

def information(request):
    """ A view to return the Public Information page """
    print('Hello, world')
    context = {

    }

    return render(request, 'information/information.html', context)

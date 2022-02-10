from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def product_detail(request):
    """ A view to return the index page """

    return render(request, 'products/product_detail.html')

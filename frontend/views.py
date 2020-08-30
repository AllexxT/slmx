from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'frontend/index.html', {})

#### Products
def forWarming(request):
    return render(request, 'frontend/products.html', {
        'title': "Смеси для утепления"
    })

def forFloor(request):
    return render(request, 'frontend/products.html', {
        'title': "Смеси для пола"
    })

def forMasonry(request):
    return render(request, 'frontend/products.html', {
        'title': "Кладочные смеси"
    })

def forCladding(request):
    return render(request, 'frontend/products.html', {
        'title': "Смеси для облицовки"
    })

def forPlaster(request):
    return render(request, 'frontend/products.html', {
        'title': "Штукатурные смеси"
    })
##########################################################

#### Product Page

def productPage(request):
    return render(request, 'frontend/productPage.html', {})

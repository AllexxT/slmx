from django.shortcuts import render
from django.template import loader
from pages.models import (
    Page
)
from catalog.models import (
    Product, Category
)


def index(request):
    content = Page.objects.get(page='index')
    categories = Category.objects.all()
    return render(
        request, 'frontend/index.html',
        {
            'content': content,
            'categories': categories
        }
    )

#### Products
def forWarming(request):
    products = Product.objects.filter(category='UT')
    content = Page.objects.get(page='smesi-dlya-utepleniya')

    return render(request, 'frontend/products.html', {
        'title': len(products),
        'content': content,
        'products': products
    })

def forFloor(request):
    products = Product.objects.filter(category='PO')
    content = Page.objects.get(page='smesi-dlya-pola')

    return render(request, 'frontend/products.html', {
        'title': '',
        'content': content,
        'products': products
    })

def forMasonry(request):
    products = Product.objects.filter(category='KL')
    content = Page.objects.get(page='kladochnye-smesi')

    return render(request, 'frontend/products.html', {
        'title': '',
        'content': content,
        'products': products
    })

def forCladding(request):
    products = Product.objects.filter(category='OB')
    content = Page.objects.get(page='smesi-dlya-oblicovki')

    return render(request, 'frontend/products.html', {
        'title': '',
        'content': content,
        'products': products
    })

def forPlaster(request):
    products = Product.objects.filter(category='SH')
    content = Page.objects.get(page='shtukaturnye-smesi')

    return render(request, 'frontend/products.html', {
        'title': '',
        'content': content,
        'products': products
    })
##########################################################

#### Product Page

def productPage(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'frontend/productPage.html', {
        'product': product
    })

from django.shortcuts import render
from django.template import loader
from pages.models import Page, OurWorks


def sertificates(request):
    content = Page.objects.get(page='sertifikaty')
    return render(
        request, 'frontend/sertificates.html',
        {
            'content': content,
            'sertificates': True,
        }
    )


def our_works(request):
    content = Page.objects.get(page='nashi-raboty')
    galleries = OurWorks.objects.all()
    return render(
        request, 'frontend/our_works.html',
        {
            'content': content,
            'ourWorks': True,
            'galleries': galleries,
        }
    )


def about(request):
    content = Page.objects.get(page='o-kompanii')
    return render(
        request, 'frontend/about.html',
        {
            'content': content,
            'about': True,
        }
    )


def contacts(request):
    content = Page.objects.get(page='kontakty')
    return render(
        request, 'frontend/contacts.html',
        {
            'content': content,
            'contacts': True,
        }
    )


def useful_info(request):
    content = Page.objects.get(page='poleznaya-informaciya')
    return render(
        request, 'frontend/useful_info.html',
        {
            'content': content,
            'usefInfo': True,
        }
    )

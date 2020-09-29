from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.templatetags.static import static
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

    def showMore(last, nxt):
        more = galleries[int(last):int(nxt)]
        moreGallery = []
        for item in more:
            print(item)
            itemDict = {
                'title': item.title,
                'address': item.address,
                'description': item.description,
                'images': []
            }
            for image in item.inpageimages_set.all():
                itemDict['images'].append({
                    'image': image.pageImage.url,
                    'thumbnail': image.pageImage.thumbnail['160x107'].url
                })
            moreGallery.append(itemDict)                
        return JsonResponse({
            'more': moreGallery
        })

    if len(request.GET) > 0:
        print(request.GET)
        if 'nxt' in request.GET:
            [last, nxt] = request.GET['last'][0], request.GET['nxt'][0]
            return showMore(last, nxt)

    return render(
        request, 'frontend/our_works.html',
        {
            'content': content,
            'ourWorks': True,
            'galleries': galleries[0:3],
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

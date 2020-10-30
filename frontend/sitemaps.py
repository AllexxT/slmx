from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from catalog.models import Product


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.all()


class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'uteplenie',
            'pol',
            'kladka',
            'oblicovka',
            'shtukaturka',
            'sertificates',
            'our_works',
            'about',
            'contacts',
            'useful_info',
        ]

    def location(self, item):
        return reverse(item)

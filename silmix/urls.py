from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from frontend.sitemaps import ProductSitemap, StaticSitemap

sitemaps = {
    'products': ProductSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),

    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

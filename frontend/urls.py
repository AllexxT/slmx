from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('smesi-dlya-utepleniya/', views.forWarming, name='uteplenie'),
    path('smesi-dlya-pola/', views.forFloor, name='pol'),
    path('kladochnye-smesi/', views.forMasonry, name='kladka'),
    path('smesi-dlya-oblicovki/', views.forCladding, name='oblicovka'),
    path('shtukaturnye-smesi/', views.forPlaster, name='shtukaturka'),
    path('product-page/', views.productPage, name='productPage'),
]

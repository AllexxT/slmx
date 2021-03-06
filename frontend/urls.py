from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('smesi-dlya-utepleniya/', views.forWarming, name='uteplenie'),
    path('smesi-dlya-utepleniya/<str:slug>', views.productPage),

    path('smesi-dlya-pola/', views.forFloor, name='pol'),
    path('smesi-dlya-pola/<str:slug>', views.productPage),

    path('kladochnye-smesi/', views.forMasonry, name='kladka'),
    path('kladochnye-smesi/<str:slug>', views.productPage),

    path('smesi-dlya-oblicovki/', views.forCladding, name='oblicovka'),
    path('smesi-dlya-oblicovki/<str:slug>', views.productPage),

    path('shtukaturnye-smesi/', views.forPlaster, name='shtukaturka'),
    path('shtukaturnye-smesi/<str:slug>', views.productPage),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('sertifikaty/', sertificates, name='sertificates'),
    path('nashi-raboty/', our_works, name='our_works'),
    path('o-kompanii/', about, name='about'),
    path('kontakty/', contacts, name='contacts'),
    path('poleznaya-informaciya/', useful_info, name='useful_info'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('familia/',Familia, name='Familia'),
    path('inicio/',inicio),
]
from django.contrib import admin
from django.urls import path, include

from catalog.views import contact, main, detail_product

urlpatterns = [
    path('', main),
    path('contact', contact),
    path('product/<pk>', detail_product),
]
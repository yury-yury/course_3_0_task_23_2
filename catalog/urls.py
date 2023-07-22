from django.contrib import admin
from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import contact, main, detail_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='catalog'),
    path('contact', contact, name='contact'),
    path('product/<pk>', detail_product, name='product'),
]
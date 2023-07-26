from django.contrib import admin
from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('contact', contact, name='contact'),
    path('product/<pk>', ProductDetailView.as_view(), name='product'),
]
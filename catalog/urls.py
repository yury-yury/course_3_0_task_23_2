from django.contrib import admin
from django.urls import path, include

from catalog.views import contact, main

urlpatterns = [
    path('', main),
    path('contact', contact),
]
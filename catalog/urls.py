from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductUpdateForModeratorView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('contact', contact, name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('update_for_moderator/<int:pk>', ProductUpdateForModeratorView.as_view(), name='update_for_moderator'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
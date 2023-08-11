from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductUpdateForModeratorView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('contact', contact, name='contact'),
    # Настройка для кеширования только контроллера
    # path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create', never_cache(ProductCreateView.as_view()), name='create'),
    path('update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='update'),
    path('update_for_moderator/<int:pk>', never_cache(ProductUpdateForModeratorView.as_view()), name='update_for_moderator'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
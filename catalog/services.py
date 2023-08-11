from typing import List

from django.core.cache import cache

from catalog.models import Category
from internet_shop.settings import CACHE_ENABLED


def get_list_category() -> List[Category]:
    if CACHE_ENABLED:
        key: str = 'categories_list'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list)
    else:
        categories_list = Category.objects.all()

    return categories_list

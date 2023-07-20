from typing import List, Dict, Any

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        cat: List[Dict[str, Any]] = [
            {"id": 1, "name": "Фрукты", "description": ""},
            {"id": 2,"name": "Овощи", "description": ""},
            {"id": 3,"name": "Крупы", "description": ""},
            {"id": 4,"name": "Макароны", "description": ""},
            {"id": 5,"name": "Конфеты", "description": ""},
        ]

        instances_list: list = []
        for item in cat:
            instances_list.append(Category(**item))

        Category.objects.bulk_create(instances_list)

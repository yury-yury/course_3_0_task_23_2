# Generated by Django 4.2.3 on 2023-08-05 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0012_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    ("set_published", "Can publish product"),
                    ("change_category", "Can change product category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
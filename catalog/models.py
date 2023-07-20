from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего обновления")

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        """
        The save function adds additional functionality to the method of the parent class. Automatically fills
        in fields when creating and editing instances of the class. After that, it calls the method of the parent class.
        """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Продукт"
        verbose_name_plural: str = "Продукты"
        ordering = ["-created_at"]


class Contact(models.Model):
    country = models.CharField(max_length=100)
    inn = models.CharField(max_length=12)
    address = models.CharField(max_length=200)

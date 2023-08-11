from django.db import models
from django.utils import timezone

from users.models import User


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
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product', default="product/default.jpg", verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего обновления")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Создатель карточки')
    is_published = models.BooleanField(default=False)

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

        permissions = [('set_published', 'Can publish product')]


class Contact(models.Model):
    country = models.CharField(max_length=100)
    inn = models.CharField(max_length=12)
    address = models.CharField(max_length=200)

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Контакт"
        verbose_name_plural: str = "Контакты"

    def __str__(self) -> str:
        return f"{self.country} ({self.address})"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    num_version = models.IntegerField(verbose_name='Номер версии товара')
    title_version = models.CharField(max_length=150, verbose_name='Название версии')
    active = models.BooleanField(default=False, verbose_name='Признак активной версии')

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Версия"
        verbose_name_plural: str = "Версии"

    def __str__(self) -> str:
        return f"Version {self.product} ({self.num_version})"
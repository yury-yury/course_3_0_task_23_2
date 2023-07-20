from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    created_at = models.DateField()
    updated_at = models.DateField()

    def save(self, *args, **kwargs):
        """
        The save function adds additional functionality to the method of the parent class. Automatically fills
        in fields when creating and editing instances of the class. After that, it calls the method of the parent class.
        """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)

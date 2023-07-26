from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    preview = models.ImageField(upload_to='blog', blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    published = models.BooleanField()
    views_count = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Запись блога"
        verbose_name_plural: str = "Записи блога"
        ordering = ["-created_at"]


from django.db import models

# Create your models here.

class TimeStampMixin(models.Model):
    """Реализация атрибутов времени создания и обновления записи"""

    created_at = models.DateTimeField("Время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления записи", auto_now=True)

    class Meta:
        abstract = True



class Bludo(TimeStampMixin):
    """Название блюда"""
    ingredients = models.ManyToManyField(
        'Ingredient', verbose_name="Ингредиенты", related_name='ingredients'
    )

    nazvanie = models.CharField("Название", max_length=50, null=False)
    prigotovlenie = models.CharField("Рецепт", max_length=500, null=False)
    image =  models.CharField("Изображение", max_length=500, null=False)

    class Meta:
        app_label = "receptsite"
        verbose_name = "блюдо"
        verbose_name_plural = "Блюдо"

    def __str__(self) -> str:
        return self.nazvanie

class Ingredient(TimeStampMixin):
    """Ингредиенты"""
    nazvanie = models.CharField("Название", max_length=50, null=False)

    def __str__(self) -> str:
        return self.nazvanie

    class Meta:
        app_label = "receptsite"
        verbose_name = "Ингредиент для блюда"
        verbose_name_plural = "Ингредиент"
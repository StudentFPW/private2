from django.db import models
# Импорт валидатора, который гарантирует, что значение поля больше или равно заданному значению.
from django.core.validators import MinValueValidator
# Импорт обратной функции из модуля django.urls.
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)

    description = models.TextField()

    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')

    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

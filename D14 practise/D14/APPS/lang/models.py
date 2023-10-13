from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=100, help_text=_('category name'))


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    kind = models.ForeignKey(Category, on_delete=models.CASCADE)

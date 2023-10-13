from django.contrib.postgres.fields import ArrayField
from django.db import models


class Author(models.Model):
    name = models.CharField(
        default='NoName',
        max_length=64,
        verbose_name='name of author'
    )


class User(models.Model):
    books = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8,
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

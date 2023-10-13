# → views.py
# Регистрация моделей категорий и продуктов на сайте администратора, иначе мы не увидим их в админке.
from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

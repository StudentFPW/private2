from .models import Category, MyModel
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(MyModel)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('name',)

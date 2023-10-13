# Импорт функции рендеринга из модуля django.shortcuts.
from django.shortcuts import render
# Импорт классов ListView и DetailView из модуля django.views.generic.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Импорт классов HttpResponse и HttpResponseRedirect из модуля django.http.
from django.http import HttpResponse, HttpResponseRedirect
# Функция, которая возвращает URL-адрес данного представления.
from django.urls import reverse_lazy
# ----------------------------------------------------------------------------------------------------------------------
# Импорт класса ProductForm из файла forms.py в том же каталоге.
from .forms import ProductForm
# ----------------------------------------------------------------------------------------------------------------------
# Импорт класса Product из файла models.py в том же каталоге.
from .models import Product
# ----------------------------------------------------------------------------------------------------------------------
# Импорт класса ProductFilter из файла filter.py в том же каталоге.
from .filters import ProductFilter


# ----------------------------------------------------------------------------------------------------------------------


class ProductsList(ListView):
    model = Product

    ordering = 'name'

    template_name = 'products.html'

    context_object_name = 'products'

    paginate_by = 2

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()

        # Используем наш класс фильтрации ProductFilter.
        # self.request.GET содержит объект QueryDict.

        # Сохраняем нашу фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ProductFilter(self.request.GET, queryset)

        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    # Переопределяем функцию
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product

    template_name = 'product.html'

    context_object_name = 'product'


# Добавляем новое представление для создания товаров.
class ProductCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm

    # модель товаров
    model = Product

    # и новый шаблон, в котором используется форма.
    template_name = 'product_edit.html'

    success_url = reverse_lazy('product_list')


# Добавляем представление для изменения товара.
class ProductUpdate(UpdateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm

    # модель товаров
    model = Product

    # и новый шаблон, в котором используется форма.
    template_name = 'product_edit.html'

    success_url = reverse_lazy('product_list')


# Представление удаляющее товар.
class ProductDelete(DeleteView):
    model = Product

    template_name = 'product_delete.html'

    success_url = reverse_lazy('product_list')


def multiply(request):
    number = request.GET.get('number')

    multiplier = request.GET.get('multiplier')

    try:
        result = int(number) * int(multiplier)
        html = f"<html><body>{number}*{multiplier}={result}</body></html>"
    except (ValueError, TypeError):
        html = f"<html><body>Invalid input.</body></html>"

    return HttpResponse(html)


def create_product(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/products/")
    return render(request, "create_product.html", {"form": form})

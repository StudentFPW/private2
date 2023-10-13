# Импорт функции рендеринга из модуля django.shortcuts.
from django.shortcuts import render
# Импорт классов ListView и DetailView из модуля django.views.generic.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Импорт классов HttpResponse и HttpResponseRedirect из модуля django.http.
from django.http import HttpResponse, HttpResponseRedirect
# Функция, которая возвращает URL-адрес данного представления.
from django.urls import reverse_lazy
# Миксин, который проверяет, вошел ли пользователь в систему. Если нет, он перенаправляет на страницу входа.
from django.contrib.auth.mixins import LoginRequiredMixin
# Проверяет, есть ли у пользователя необходимые разрешения. Если нет, он перенаправляет на страницу входа.
from django.contrib.auth.mixins import PermissionRequiredMixin

# ----------------------------------------------------------------------------------------------------------------------
# Импорт класса ProductForm из файла forms.py в том же каталоге.
from .forms import ProductForm
# ----------------------------------------------------------------------------------------------------------------------
# Импорт класса Product из файла models.py в том же каталоге.
from .models import Product
# ----------------------------------------------------------------------------------------------------------------------
# Импорт класса ProductFilter из файла filter.py в том же каталоге.
from .filters import ProductFilter


class ProductsList(ListView):
    model = Product

    ordering = 'name'

    template_name = 'products.html'

    context_object_name = 'products'

    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = ProductFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product

    template_name = 'product.html'

    context_object_name = 'product'


class ProductCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    # Проверка наличия у пользователя прав на добавление товара.
    permission_required = ('app.add_product',)
    # Если пользователь не вошел в систему, это вызовет исключение.
    # raise_exception = True

    form_class = ProductForm

    model = Product

    template_name = 'product_edit.html'

    success_url = reverse_lazy('product_list')


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    # Проверка наличия у пользователя прав на изменение продукта.
    permission_required = ('app.change_product',)

    form_class = ProductForm

    model = Product

    template_name = 'product_edit.html'

    success_url = reverse_lazy('product_list')


class ProductDelete(PermissionRequiredMixin, DeleteView):
    # Проверка наличия у пользователя прав на удаление продукта.
    permission_required = ('app.delete_product',)

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

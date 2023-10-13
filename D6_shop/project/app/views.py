# Декоратор, проверяющий действительный токен CSRF. Если токен отсутствует или недействителен, вернет ошибку HTTP 403.
from django.views.decorators.csrf import csrf_protect
# Декоратор, который проверяет, вошел ли пользователь в систему. Если нет, он перенаправляет на страницу входа.
from django.contrib.auth.decorators import login_required
# Способ проверить, подписан ли пользователь на категорию.
from django.db.models import Exists, OuterRef
# Импорт функции рендеринга из модуля django.shortcuts.
from django.shortcuts import render
# Импорт классов из модуля django.views.generic.
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
from .models import Product, Category, Subscription
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
    permission_required = ('app.add_product',)

    form_class = ProductForm

    model = Product

    template_name = 'product_edit.html'

    success_url = reverse_lazy('product_list')


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('app.change_product',)

    form_class = ProductForm

    model = Product

    template_name = 'product_edit.html'

    success_url = reverse_lazy('product_list')


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('app.delete_product',)

    model = Product

    template_name = 'product_delete.html'

    success_url = reverse_lazy('product_list')


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(user=request.user, category=category, ).delete()

    categories_with_subscriptions = Category.objects.annotate(user_subscribed=Exists(
        Subscription.objects.filter(
            user=request.user,
            category=OuterRef('pk'), ))).order_by('name')

    return render(request, 'subscriptions.html', {'categories': categories_with_subscriptions}, )


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

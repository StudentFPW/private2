from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import ProductForm
from .models import Product, Category, Subscription, Order
from .filters import ProductFilter
from Task.tasks import complete_order


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


class IndexView(TemplateView):
    template_name = "index_main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        return context


# форма нового заказа
class NewOrderView(CreateView):
    model = Order
    fields = ['products']  # единственное поле
    template_name = 'order.html'

    # после валидации формы, сохраняем объект,
    # считаем его общую стоимость
    # и вызываем задачу "завершить заказ" через минуту после вызова
    def form_valid(self, form):
        order = form.save()
        order.cost = sum([prod.price for prod in order.products.all()])
        order.save()
        complete_order.apply_async([order.pk], countdown=60)
        return redirect('/')


# представление для "кнопки", чтобы можно было забрать заказ
def take_order(request, oid):
    order = Order.objects.get(pk=oid)
    order.time_out = datetime.now()
    order.save()
    return redirect('/')

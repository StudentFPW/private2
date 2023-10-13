from django.urls import path
from .views import ProductsList, \
    ProductDetail, \
    ProductCreate, \
    ProductUpdate, \
    ProductDelete, \
    multiply, \
    create_product, \
    subscriptions, \
    NewOrderView, \
    take_order, \
    IndexView

urlpatterns = [
    path('products/', ProductsList.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),

    path('products/create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),

    path('multiply/', multiply),
    path("upload/", create_product),
    path('products/subscriptions/', subscriptions, name='subscriptions'),
    path("", IndexView.as_view()),
    path('new/', NewOrderView.as_view(), name='new_order'),
    path('take/<int:oid>', take_order, name='take_order')
]

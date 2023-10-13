from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreate, ProductUpdate, multiply, create_product, ProductDelete

urlpatterns = [
    path('products/', ProductsList.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('multiply/', multiply),
    path("upload/", create_product),
]

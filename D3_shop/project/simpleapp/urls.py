# → project\urls.py
from django.urls import path
# Импортируем созданные нами представления
from .views import ProductsList, ProductDetail

urlpatterns = [
    # as_view() метод, который возвращает функцию представления.
    path('', ProductsList.as_view()),
    # Это шаблон URL, который соответствует целому числу и передает его представлению в качестве
    # аргумента ключевого слова с именем pk.
    path('<int:pk>', ProductDetail.as_view()),
]

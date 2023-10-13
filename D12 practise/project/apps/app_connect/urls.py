from django.urls import path
from .views import SimpleView

urlpatterns = [
    path('request/', SimpleView.as_view()),
]

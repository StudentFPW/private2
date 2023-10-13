from django.urls import path
from .views import Index1, Index2, set_timezone, Index

urlpatterns = [
    path('lang1/', Index1.as_view()),
    path("lang2/", Index2.as_view()),
    path("time1/", set_timezone, name="set_timezone"),
    path("time2/", Index.as_view(), name="time"),
]

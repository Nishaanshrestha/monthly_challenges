
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path("<month>/",views.months_challenges)
]
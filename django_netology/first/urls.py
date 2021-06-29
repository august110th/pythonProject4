from django.contrib import admin
from django.urls import path, include

from django_netology.first.views import home_view

urlpatterns = [
    path("home", home_view, name="")
]

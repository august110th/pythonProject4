from django.contrib import admin
from django.urls import path, include

from django_netology.first.views import home_view

urlpatterns = {
    path('admin/', admin.site.urls),
    path("", include("first.url.py"))
}

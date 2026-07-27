# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    # API navegable de DRF (login/logout en el navegador)
    path("api-auth/", include("rest_framework.urls")),
]

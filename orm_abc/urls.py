"""
Корневая URL-конфигурация проекта orm_abc.

Список urlpatterns направляет URL-адреса к соответствующим представлениям.

Документация: https://docs.djangoproject.com/en/5.2/topics/http/urls/

"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Административный интерфейс Django: http://127.0.0.1:8000/admin/
    # Доступ: createsuperuser → логин/пароль
    path("admin/", admin.site.urls, name="admin"),

    # Подключаем URL-маршруты приложения orm_abc_app к корневому пути.
    # Все маршруты из orm_abc_app/urls.py доступны с корня сайта (/).
    path("", include("orm_abc_app.urls")),
]

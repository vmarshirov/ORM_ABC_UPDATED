"""
URL-конфигурация приложения orm_abc_app.

Этот файл подключается к корневым URLs проекта через include() в orm_abc/urls.py.

app_name позволяет использовать пространство имён при разрешении URL:
    {% url 'orm_abc_app:index' %}       — в шаблоне
    reverse('orm_abc_app:abc_result')   — в Python-коде

Документация по URL: https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.urls import path

from . import views

# Пространство имён (namespace) для URL этого приложения.
# Позволяет избежать конфликтов имён при наличии нескольких приложений.
app_name = "orm_abc_app"

urlpatterns = [
    # Главная страница — список ссылок на документацию
    # URL: http://127.0.0.1:8000/
    path("", views.index, name="index"),

    # Страница демонстрации даты и времени
    # URL: http://127.0.0.1:8000/datetime_nov/
    path("datetime_nov/", views.datetime_nov, name="datetime_nov"),

    # Страница демонстрации переменных, списков и словарей в шаблоне
    # URL: http://127.0.0.1:8000/var_list_dict/
    path("var_list_dict/", views.var_list_dict, name="var_list_dict"),

    # Страница с простой формой (Form, не ModelForm)
    # URL: http://127.0.0.1:8000/abc_form/
    path("abc_form/", views.abc_form, name="abc_form"),

    # Обработчик GET-данных из abc_form (сохранение + редирект)
    # URL: http://127.0.0.1:8000/abc_get/?task=...&a=1&b=2&c=3
    path("abc_get/", views.abc_get, name="abc_get"),

    # Страница с ModelForm (стандартное отображение Django)
    # URL: http://127.0.0.1:8000/abc_model_form/
    path("abc_model_form/", views.abc_model_form, name="abc_model_form"),

    # Страница с ModelForm, оформленной через django-widget-tweaks
    # URL: http://127.0.0.1:8000/abc_tweaks_form/
    path("abc_tweaks_form/", views.abc_tweaks_form, name="abc_tweaks_form"),

    # Страница результатов — последняя запись и вычисление C = A+B
    # URL: http://127.0.0.1:8000/abc_result/
    path("abc_result/", views.abc_result, name="abc_result"),

    # Страница таблицы — все записи и агрегатная статистика
    # URL: http://127.0.0.1:8000/table/
    path("table/", views.table, name="table"),
]

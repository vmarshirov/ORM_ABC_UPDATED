"""
Регистрация моделей в административном интерфейсе Django.

Административный интерфейс доступен по адресу: http://127.0.0.1:8000/admin/
Для входа нужно создать суперпользователя:
    python manage.py createsuperuser

Документация по admin: https://docs.djangoproject.com/en/5.2/ref/contrib/admin/
"""

from django.contrib import admin

from .models import AbcModel


@admin.register(AbcModel)
class AbcModelAdmin(admin.ModelAdmin):
    """
    Настройки отображения модели AbcModel в административном интерфейсе.

    Атрибуты:
        list_display    — поля, видимые в списке записей
        list_editable   — поля, редактируемые прямо в списке (без входа в запись)
        search_fields   — поля, по которым работает строка поиска
        list_filter     — поля для фильтрации в правой панели
        list_per_page   — количество записей на странице
        readonly_fields — поля, доступные только для чтения
        ordering        — порядок сортировки по умолчанию в admin
    """

    # Столбцы, отображаемые в списке записей
    list_display = ["id", "task", "a", "b", "c", "result", "current_date"]

    # Поля, которые можно редактировать прямо из списка записей
    list_editable = ["task"]

    # Строка поиска: ищет совпадения в указанных полях
    search_fields = ["task", "result"]

    # Фильтры в правой боковой панели
    list_filter = ["c", "current_date"]

    # Количество записей на одной странице списка
    list_per_page = 20

    # Поля только для чтения (не редактируются через admin)
    # current_date имеет auto_now=True, Django запрещает его редактирование
    readonly_fields = ["current_date", "result"]

    # Порядок сортировки: новые записи первыми
    ordering = ["-pk"]

"""
Конфигурация приложения orm_abc_app.

Класс AppConfig хранит метаданные приложения и позволяет выполнять
инициализационный код при запуске Django (метод ready()).

Документация: https://docs.djangoproject.com/en/5.2/ref/applications/
"""

from django.apps import AppConfig


class OrmAbcAppConfig(AppConfig):
    """
    Конфигурация приложения orm_abc_app.

    Атрибуты:
        default_auto_field — тип первичного ключа по умолчанию для моделей
                             этого приложения (переопределяет DEFAULT_AUTO_FIELD
                             из settings.py на уровне приложения)
        name               — Python-путь к пакету приложения
        verbose_name       — человекочитаемое название в административном интерфейсе
    """

    # BigAutoField — 64-битный автоинкрементный первичный ключ (рекомендуется)
    default_auto_field = "django.db.models.BigAutoField"

    # Должно совпадать с именем папки приложения
    name = "orm_abc_app"

    # Отображаемое название в панели администратора
    verbose_name = "ORM ABC — учебное приложение"

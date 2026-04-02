#!/usr/bin/env python
"""
Утилита командной строки Django для выполнения административных задач.

Использование:
    python manage.py runserver          # запуск сервера разработки
    python manage.py makemigrations     # создание миграций
    python manage.py migrate            # применение миграций
    python manage.py createsuperuser    # создание суперпользователя
    python manage.py shell              # интерактивная Django-оболочка

Документация: https://docs.djangoproject.com/en/5.2/ref/django-admin/
"""

import os
import sys


def main():
    """
    Точка входа для административных команд Django.

    Устанавливает переменную окружения DJANGO_SETTINGS_MODULE,
    если она ещё не задана, и выполняет команду из аргументов командной строки.
    """
    # Указываем модуль настроек по умолчанию
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_abc.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Если Django не установлен или виртуальная среда не активирована
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен "
            "и доступен в переменной окружения PYTHONPATH. "
            "Возможно, вы забыли активировать виртуальную среду?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

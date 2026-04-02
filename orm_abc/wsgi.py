"""
WSGI-конфигурация для проекта orm_abc.

Предоставляет WSGI-совместимый объект приложения в переменной ``application``.

WSGI (Web Server Gateway Interface) — стандартный интерфейс между
веб-серверами (Gunicorn, uWSGI, Apache mod_wsgi) и Python-приложениями.

Документация: https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Указываем модуль настроек, который Django будет использовать.
# ИСПРАВЛЕНО: в оригинале было 'abc_prj.settings' (неверно).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_abc.settings")

# Создаём WSGI-приложение, которое будет обрабатывать HTTP-запросы
application = get_wsgi_application()

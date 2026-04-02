"""
ASGI-конфигурация для проекта orm_abc.

Предоставляет ASGI-совместимый объект приложения в переменной ``application``.

ASGI (Asynchronous Server Gateway Interface) — современный стандарт,
расширяющий WSGI для поддержки асинхронных возможностей: WebSockets,
HTTP/2, long-polling и т.д.

Документация: https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Указываем модуль настроек, который Django будет использовать.
# ИСПРАВЛЕНО: в оригинале было 'orm_abc_prj.settings' (неверно).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_abc.settings")

# Создаём ASGI-приложение
application = get_asgi_application()

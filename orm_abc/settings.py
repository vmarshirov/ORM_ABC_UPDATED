"""
Настройки Django для проекта orm_abc.

Обновлено до Django 5.2 LTS.
Документация по настройкам: https://docs.djangoproject.com/en/5.2/topics/settings/
Полный список параметров:  https://docs.djangoproject.com/en/5.2/ref/settings/

ВАЖНО: Перед деплоем в продакшн обязательно ознакомьтесь с чеклистом:
    https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Пути
# ---------------------------------------------------------------------------

# Корневой каталог проекта (родитель папки orm_abc/)
# Path(__file__) → .../orm_abc/settings.py
# .resolve()     → абсолютный путь
# .parent.parent → два уровня вверх = корень проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# Безопасность
# ---------------------------------------------------------------------------

# Секретный ключ для криптографических операций Django (CSRF, сессии и т.д.).
# ВНИМАНИЕ: В продакшн-среде обязательно:
#   1. Замените этот ключ на уникальный
#   2. Храните его в переменной окружения, а не в коде
#   3. Никогда не публикуйте в системах контроля версий
SECRET_KEY = "django-insecure-)wgx)3x(wrs4%=(*^)cw6rps*t*#98dd(l%r#o8ktg$^+lpuy8"

# Режим отладки. В продакшне ОБЯЗАТЕЛЬНО установите DEBUG = False.
# При DEBUG=True Django показывает подробные страницы ошибок и
# обслуживает статические файлы самостоятельно.
DEBUG = True

# Список хостов/доменов, для которых может работать этот Django-сайт.
# При DEBUG=True Django разрешает запросы от localhost автоматически.
# В продакшне нужно указать явно: ['mysite.com', 'www.mysite.com']
ALLOWED_HOSTS = []


# ---------------------------------------------------------------------------
# Приложения
# ---------------------------------------------------------------------------

INSTALLED_APPS = [
    # Стандартные приложения Django
    "django.contrib.admin",        # Административный интерфейс
    "django.contrib.auth",         # Система аутентификации и авторизации
    "django.contrib.contenttypes", # Фреймворк типов контента
    "django.contrib.sessions",     # Фреймворк сессий
    "django.contrib.messages",     # Фреймворк сообщений (flash-messages)
    "django.contrib.staticfiles",  # Управление статическими файлами

    # Приложение проекта
    "orm_abc_app.apps.OrmAbcAppConfig",

    # Сторонние библиотеки
    "widget_tweaks",  # Настройка виджетов форм в шаблонах ({% render_field %})
]


# ---------------------------------------------------------------------------
# Промежуточное ПО (Middleware)
# ---------------------------------------------------------------------------

# Middleware обрабатывают запросы/ответы в порядке списка (запрос) /
# обратном порядке (ответ).
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",           # Заголовки безопасности
    "django.contrib.sessions.middleware.SessionMiddleware",    # Поддержка сессий
    "django.middleware.common.CommonMiddleware",               # Базовые HTTP-возможности
    "django.middleware.csrf.CsrfViewMiddleware",              # Защита от CSRF-атак
    "django.contrib.auth.middleware.AuthenticationMiddleware", # Аутентификация пользователей
    "django.contrib.messages.middleware.MessageMiddleware",    # Flash-сообщения
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Защита от clickjacking
]


# ---------------------------------------------------------------------------
# URL-маршрутизация
# ---------------------------------------------------------------------------

# Модуль с корневыми URL-паттернами проекта
ROOT_URLCONF = "orm_abc.urls"


# ---------------------------------------------------------------------------
# Шаблоны
# ---------------------------------------------------------------------------

TEMPLATES = [
    {
        # Движок шаблонов Django (DTL — Django Template Language)
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # Дополнительные каталоги для поиска шаблонов (помимо app/templates/)
        "DIRS": [],

        # Автоматически искать шаблоны в папке templates/ каждого приложения
        "APP_DIRS": True,

        "OPTIONS": {
            # Контекстные процессоры добавляют переменные в каждый шаблон
            "context_processors": [
                "django.template.context_processors.debug",    # {{ debug }}
                "django.template.context_processors.request",  # {{ request }}
                "django.contrib.auth.context_processors.auth", # {{ user }}, {{ perms }}
                "django.contrib.messages.context_processors.messages",  # {{ messages }}
            ],
        },
    },
]

# Можно добавить настройку для отключения темы в админке
ADMIN_THEME_ENABLED = False  # Отключаем тему в админке

# ---------------------------------------------------------------------------
# WSGI / ASGI
# ---------------------------------------------------------------------------

# Точка входа для WSGI-серверов (Gunicorn, uWSGI)
WSGI_APPLICATION = "orm_abc.wsgi.application"


# ---------------------------------------------------------------------------
# База данных
# ---------------------------------------------------------------------------

# SQLite — встроенная СУБД, не требует дополнительной установки.
# Подходит для разработки и учебных проектов.
# Для продакшна рекомендуется PostgreSQL или MySQL.
# Документация: https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # Файл базы данных в корне проекта
    }
}


# ---------------------------------------------------------------------------
# Валидация паролей
# ---------------------------------------------------------------------------

# Набор валидаторов для проверки надёжности паролей пользователей.
# Документация: https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        # Пароль не должен быть слишком похож на атрибуты пользователя
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        # Минимальная длина пароля (по умолчанию 8 символов)
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        # Пароль не должен быть из списка распространённых
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        # Пароль не должен состоять только из цифр
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ---------------------------------------------------------------------------
# Интернационализация
# ---------------------------------------------------------------------------

# Документация: https://docs.djangoproject.com/en/5.2/topics/i18n/

# Код языка интерфейса (влияет на переводы Django, форматы дат и т.д.)
LANGUAGE_CODE = "ru-ru"

# Часовой пояс для хранения и отображения дат
# Список: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = "Europe/Moscow"

# Включить поддержку перевода интерфейса
USE_I18N = True

# Использовать часовые пояса (datetime-объекты будут timezone-aware)
USE_TZ = True


# ---------------------------------------------------------------------------
# Статические файлы (CSS, JavaScript, изображения)
# ---------------------------------------------------------------------------

# URL-префикс для статических файлов
# Документация: https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = "static/"


# ---------------------------------------------------------------------------
# Первичные ключи
# ---------------------------------------------------------------------------

# Тип поля первичного ключа по умолчанию для новых моделей.
# BigAutoField — 64-битное целое (от 1 до 9 223 372 036 854 775 807)
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

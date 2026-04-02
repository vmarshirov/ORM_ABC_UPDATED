## Быстрый старт

```bash
# 1. Создать и активировать виртуальную среду
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate     # Windows

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Применить миграции
python manage.py migrate

# 4. Создать суперпользователя (для /admin/)
python manage.py createsuperuser

# 5. Запустить сервер разработки
python manage.py runserver
```

Приложение доступно по адресу: **http://127.0.0.1:8000/**

---

## Структура проекта

```
orm_abc/                    ← настройки проекта
    settings.py             ← конфигурация Django 5.2
    urls.py                 ← корневые URL-маршруты
    wsgi.py / asgi.py       ← WSGI/ASGI точки входа

orm_abc_app/                ← основное приложение
    models.py               ← модель AbcModel
    views.py                ← представления (8 функций)
    forms.py                ← AbcForm + AbcModelForm
    urls.py                 ← URL-маршруты приложения
    admin.py                ← настройки административного интерфейса
    ORM.py                  ← обучающий скрипт для Django shell
    migrations/
        0001_initial.py     ← единая сжатая начальная миграция
    templates/              ← HTML-шаблоны
    static/css/             ← стили
    static/images/          ← изображения

requirements.txt            ← зависимости проекта
```

---

## Полезные команды Django Shell

```
# Запуск:
python manage.py shell
from orm_abc_app.models import AbcModel

# Создание
AbcModel.objects.create(task='Тест', a=1, b=2, c=10)

# Чтение
AbcModel.objects.all()
AbcModel.objects.filter(c=10).values('id', 'task', 'a', 'b', 'c')
```

Подробнее — в файле `orm_abc_app/ORM.py`.

---

## Документация Django 5.2

- [Модели](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [QuerySet API](https://docs.djangoproject.com/en/5.2/ref/models/querysets/)
- [Формы](https://docs.djangoproject.com/en/5.2/topics/forms/)
- [Шаблоны](https://docs.djangoproject.com/en/5.2/ref/templates/language/)
- [Административный интерфейс](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

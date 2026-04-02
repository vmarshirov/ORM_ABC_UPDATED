# orm_abc — Учебный проект Django ORM

Учебный проект для изучения Django ORM и форм.
Обновлён до **Django 5.2 LTS**, приведён к стандарту **PEP 8**,
снабжён подробными комментариями к коду.

---

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

## Страницы приложения

| URL | Описание |
|-----|----------|
| `/` | Главная страница со ссылками на документацию |
| `/datetime_nov/` | Демонстрация даты и времени в шаблоне |
| `/var_list_dict/` | Переменные, списки и словари в шаблоне |
| `/abc_form/` | Простая форма (Form, GET-метод) |
| `/abc_model_form/` | ModelForm (стандартное отображение) |
| `/abc_tweaks_form/` | ModelForm с django-widget-tweaks |
| `/abc_result/` | Результат проверки C = A + B |
| `/table/` | Таблица всех записей и статистика |
| `/admin/` | Административный интерфейс Django |

---

## Изменения относительно оригинала

### Исправленные ошибки
- **`wsgi.py`**: неверное имя модуля настроек `abc_prj.settings` → `orm_abc.settings`
- **`asgi.py`**: неверное имя модуля `orm_abc_prj.settings` → `orm_abc.settings`
- **`abc_model_form.html`**: дублирующаяся кавычка `action= "...""`
- **`abc_tweaks_form.html`**: отсутствовал атрибут `action=` в теге `<form>`
- **`abc_form.html`**: опечатка `metod='get'` → `method="get"`
- **`table.html`**: незакрытый `<tbody>` вместо `</tbody>` (×2)
- **`layout.html`**: тег `<body>` был расположен после `<div>` — невалидный HTML
- **`views.py`**: `abc_result` падал с исключением при пустой БД
- **`views.py`**: `abc_get` не обрабатывал ошибки при нечисловых параметрах

### Обновления
- Django **4.1.7** → **5.2 LTS**
- Bootstrap **5.1.3** → **5.3.3**
- Все ссылки на документацию обновлены до версии 5.2
- 22 исторические миграции сжаты в 1 чистую начальную миграцию
- `admin.py` — полная конфигурация `ModelAdmin` вместо минимальной
- Добавлены базовые тесты в `tests.py`

### Стиль кода (PEP 8)
- Все строки — не длиннее 79 символов (где возможно)
- Одинарные кавычки заменены на двойные (стандарт black/PEP 8)
- Убраны лишние пробелы и пустые строки
- Импорты сгруппированы: stdlib → Django → локальные

---

## Полезные команды Django Shell

```python
# Запуск: python manage.py shell
from orm_abc_app.models import AbcModel

# Создание
AbcModel.objects.create(task='Тест', a=1, b=2, c=10)

# Чтение
AbcModel.objects.all()
AbcModel.objects.filter(c=10).values('id', 'task', 'a', 'b', 'c')

# Агрегация
from django.db.models import Sum, Avg
AbcModel.objects.aggregate(Sum('b'), Avg('b'))
```

Подробнее — в файле `orm_abc_app/ORM.py`.

---

## Документация Django 5.2

- [Модели](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [QuerySet API](https://docs.djangoproject.com/en/5.2/ref/models/querysets/)
- [Формы](https://docs.djangoproject.com/en/5.2/topics/forms/)
- [Шаблоны](https://docs.djangoproject.com/en/5.2/ref/templates/language/)
- [Административный интерфейс](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

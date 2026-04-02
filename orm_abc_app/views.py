"""
Представления (views) приложения orm_abc_app.

Каждая функция-представление принимает объект HttpRequest и возвращает
HttpResponse (или его подкласс). Представления вызываются маршрутизатором
Django согласно urls.py.

Документация по представлениям: https://docs.djangoproject.com/en/5.2/topics/http/views/
Документация по QuerySet API:    https://docs.djangoproject.com/en/5.2/ref/models/querysets/
"""

import datetime

from django.db.models import Avg, Count, Max, Min, StdDev, Sum
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render

from .forms import AbcForm, AbcModelForm
from .models import AbcModel


# ---------------------------------------------------------------------------
# Вспомогательные функции
# ---------------------------------------------------------------------------

def solution(a, b, c):
    """
    Проверяет, равно ли значение C сумме A и B.

    Args:
        a (int): первое слагаемое
        b (int): второе слагаемое
        c (int): проверяемая сумма

    Returns:
        str: текстовый результат проверки на русском языке

    Примеры:
        >>> solution(2, 3, 5)
        'С равна сумме A и B'
        >>> solution(1, 1, 3)
        'С не равна сумме A и B'
    """
    if a + b == c:
        return "С равна сумме A и B"
    return "С не равна сумме A и B"


# ---------------------------------------------------------------------------
# Представления — информационные страницы
# ---------------------------------------------------------------------------

def index(request):
    """
    Главная страница приложения.
    Отображает список полезных ссылок на документацию Django ORM.
    """
    return render(request, "index.html")


def datetime_nov(request):
    """
    Страница демонстрации работы с датой и временем.
    Передаёт текущие дату и время в шаблон через контекст.
    Показывает, как Python-объект datetime отображается в шаблоне Django.
    """
    # Получаем текущую дату и время (без учёта часового пояса)
    datetime_now = datetime.datetime.now()
    print(f"[datetime_nov] datetime_now = {datetime_now}")

    # Передаём дату в шаблон под ключом 'key'
    context = {"key": datetime_now}
    return render(request, "datetime_now.html", context)


def var_list_dict(request):
    """
    Страница демонстрации работы с переменными, списками и словарями в шаблоне.

    Передаёт в шаблон:
        var_main  (int)  — простая переменная
        list_main (list) — список значений
        dict_main (dict) — словарь с ключами x и y
    """
    var_main = 2
    list_main = [1, 2, 3, 4, 5]
    dict_main = {"x": 1, "y": 2}

    print(f"var_list_dict:  var_main={var_main}, list_main={list_main}, dict_main={dict_main}")

    context = {
        "var_main": var_main,
        "list_main": list_main,
        "dict_main": dict_main,
    }
    return render(request, "list_dict.html", context)


# ---------------------------------------------------------------------------
# Представления — формы
# ---------------------------------------------------------------------------

def abc_form(request):
    """
    Страница с простой HTML-формой (не привязанной к модели).
    Создаёт экземпляр AbcForm с начальными значениями и передаёт его
    в шаблон. Форма отправляется методом GET в представление abc_get.
    Документация по формам: https://docs.djangoproject.com/en/5.2/topics/forms/
    """
    # Создаём несвязанную  форму с начальными значениями из класса
    form = AbcForm()
    print(f"[abc_form] form = \n {form}")

    return render(request, "abc_form.html", {"abc_form": form})


def abc_get(request):
    """
    Обработчик GET-запроса из abc_form.

    Читает параметры task, a, b, c из строки запроса (GET-параметры),
    создаёт новую запись AbcModel и перенаправляет на страницу результатов.

    Пример URL: /abc_get/?task=...&a=1&b=2&c=3

    ВАЖНО: GET-метод не подходит для изменения данных в продакшне
    (нарушает семантику HTTP). Используется здесь только в учебных целях.
    """
    print(f"[abc_get] GET-параметры: {request.GET}")

    # Безопасно извлекаем параметры из строки запроса
    task_value = request.GET.get("task", "")

    # Проверяем наличие обязательных числовых параметров
    try:
        a_value = int(request.GET.get("a", 0))
        b_value = int(request.GET.get("b", 0))
        c_value = int(request.GET.get("c", 0))
    except (TypeError, ValueError):
        # Если параметры не являются числами — возвращаем ошибку 400
        return HttpResponseBadRequest("Параметры a, b, c должны быть целыми числами.")

    print(f"[abc_get] a={a_value}, b={b_value}, c={c_value}")

    # Создаём новую запись в базе данных
    new_obj = AbcModel(task=task_value, a=a_value, b=b_value, c=c_value)
    new_obj.save()

    # Перенаправляем на страницу результатов
    return redirect("orm_abc_app:abc_result")


def abc_model_form(request):
    """
    Страница с ModelForm — формой, напрямую связанной с моделью AbcModel.

    При POST-запросе:
        - Валидирует данные формы
        - Если форма валидна — сохраняет запись и перенаправляет на результаты
        - Если не валидна — повторно отображает форму с ошибками

    При GET-запросе:
        - Отображает пустую форму с начальными значениями модели

    Документация по ModelForm: https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/
    """
    print(f"[abc_model_form] метод запроса: {request.method}")

    if request.method == "POST":
        # Связываем форму с данными из POST-запроса
        form = AbcModelForm(request.POST)
        if form.is_valid():
            # Данные прошли валидацию — сохраняем в базу
            print(f"[abc_model_form] форма валидна: {form.cleaned_data}")
            form.save()
            return redirect("orm_abc_app:abc_result")
        # Форма невалидна — Django автоматически добавит ошибки в объект form
        print(f"[abc_model_form] форма невалидна: {form.errors}")
    else:
        # GET-запрос — создаём пустую форму
        form = AbcModelForm()
        print(f"[abc_model_form] пустая форма: {form}")

    return render(request, "abc_model_form.html", {"form": form})


def abc_tweaks_form(request):
    """
    Страница с ModelForm, оформленной через библиотеку django-widget-tweaks.

    Функционально идентична abc_model_form, но шаблон использует
    тег {% render_field %} для гибкого управления CSS-классами виджетов
    без изменения кода Python.

    Документация widget-tweaks: https://pypi.org/project/django-widget-tweaks/
    """
    print(f"[abc_tweaks_form] метод запроса: {request.method}")

    if request.method == "POST":
        form = AbcModelForm(request.POST)
        if form.is_valid():
            print(f"[abc_tweaks_form] форма валидна: {form.cleaned_data}")
            form.save()
            return redirect("orm_abc_app:abc_result")
        print(f"[abc_tweaks_form] форма невалидна: {form.errors}")
    else:
        form = AbcModelForm()
        print(f"[abc_tweaks_form] пустая форма: {form}")

    return render(request, "abc_tweaks_form.html", {"form": form})


# ---------------------------------------------------------------------------
# Представления — результаты и таблица
# ---------------------------------------------------------------------------

def abc_result(request):
    """
    Страница результатов: отображает последнюю запись и вычисляет C == A+B.

    Шаги:
        1. Получает все записи, отсортированные по убыванию id
        2. Берёт последнюю добавленную запись (первую в отсортированном списке)
        3. Вычисляет результат с помощью solution()
        4. Обновляет поле result в базе данных
        5. Передаёт данные в шаблон

    Использует:
        - QuerySet.values()      — получить словарь полей
        - QuerySet.values_list() — получить кортеж значений
        - QuerySet.update()      — обновить запись
    """
    # Получаем все объекты, новые — первыми
    object_list = AbcModel.objects.all().order_by("-id")
    print(f"\n[abc_result] object_list: {object_list}")

    # Берём последнюю запись как словарь нужных полей
    last_object = object_list.values("task", "a", "b", "c").first()
    if last_object is None:
        # Если записей нет — перенаправляем на форму
        return redirect("orm_abc_app:abc_model_form")

    # Получаем ID последней записи для последующего обновления
    task_id = object_list.values("id").first()["id"]
    print(f"[abc_result] task_id={task_id}, last_object={last_object}")

    # Вычисляем результат
    result = solution(last_object["a"], last_object["b"], last_object["c"])
    print(f"[abc_result] result: {result}")

    # Обновляем поле result в базе данных
    AbcModel.objects.filter(id=task_id).update(result=result)

    # Получаем кортеж значений для альтернативного отображения в шаблоне
    # values_list() возвращает QuerySet кортежей: (id, task, a, b, c, result, date)
    values_tuple = object_list.values_list().first()
    task_formulation = values_tuple[1]  # индекс 1 — поле task
    # Извлекаем a, b, c, result (индексы 2, 3, 4, 5)
    last_values = list(values_tuple[2:6])
    print(f"[abc_result] task_formulation={task_formulation}, last_values={last_values}")

    context = {
        "last_object": last_object,         # словарь {task, a, b, c}
        "task_formulation": task_formulation, # строка — формулировка задачи
        "last_values": last_values,           # список [a, b, c, result]
        "result": result,                     # строка — текст результата
    }
    return render(request, "abc_result.html", context)


def table(request):
    """
    Страница таблицы: отображает все записи и статистику по полю B.

    Демонстрирует:
        - objects.values()          — все записи как список словарей
        - objects.values_list()     — все записи как список кортежей
        - .filter() + .order_by()   — фильтрация и сортировка
        - .aggregate(Count|Avg|...) — агрегатные функции
        - _meta.get_fields()        — динамическое получение имён полей
    """
    # Получаем все записи как QuerySet словарей (для первой таблицы)
    objects_values = AbcModel.objects.values()
    print(f"\n[table] objects_values: {objects_values}")

    # Получаем отфильтрованные записи как QuerySet кортежей (для второй таблицы)
    # filter(id__gte=2) — записи с id >= 2; order_by("-id") — новые первыми
    objects_values_list = (
        AbcModel.objects.values_list()
        .filter(id__gte=2)
        .order_by("-id")
    )
    print(f"[table] objects_values_list: {objects_values_list}")

    cur_objects = objects_values_list

    # Агрегатная статистика по полю B.
    # aggregate() возвращает словарь вида {'b__count': N} и т.д.
    statics_val = [
        cur_objects.aggregate(Count("b")),   # количество непустых значений B
        cur_objects.aggregate(Avg("b")),     # среднее значение B
        cur_objects.aggregate(Min("b")),     # минимальное значение B
        cur_objects.aggregate(Max("b")),     # максимальное значение B
        cur_objects.aggregate(StdDev("b")), # стандартное отклонение B
        cur_objects.aggregate(Sum("b")),     # сумма значений B
    ]
    print(f"[table] statics_val: {statics_val}")

    # Получаем метаданные модели: список объектов Field
    fields = AbcModel._meta.get_fields()
    print(f"[table] fields: {fields}")

    # Собираем списки machine-name и verbose_name для заголовков таблиц
    verbose_name_list = []
    name_list = []
    for field in fields:
        verbose_name_list.append(field.verbose_name)
        name_list.append(field.name)

    print(f"[table] verbose_name_list: {verbose_name_list}")
    print(f"[table] name_list: {name_list}")

    context = {
        "objects_values": objects_values,           # все записи (словари)
        "name_list": name_list,                     # технические имена полей
        "objects_values_list": objects_values_list, # отфильтрованные (кортежи)
        "verbose_name_list": verbose_name_list,     # читаемые имена полей
        "statics": {"statics_val": statics_val},   # словарь со статистикой
        "field_names": verbose_name_list,           # псевдоним для шаблона
    }
    return render(request, "table.html", context)

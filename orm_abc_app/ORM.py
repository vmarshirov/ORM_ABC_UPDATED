"""
Обучающий скрипт: демонстрация Django ORM QuerySet API.

Этот файл НЕ предназначен для выполнения как обычный Python-скрипт.
Он содержит набор примеров команд для Django-оболочки.

Запуск Django-оболочки:
    python manage.py shell

Затем в оболочке можно копировать и выполнять блоки кода ниже.

Документация QuerySet API: https://docs.djangoproject.com/en/5.2/ref/models/querysets/
Документация по моделям:   https://docs.djangoproject.com/en/5.2/ref/models/
Поля моделей:              https://docs.djangoproject.com/en/5.2/ref/models/fields/
Запросы к БД:              https://docs.djangoproject.com/en/5.2/topics/db/queries/
Сложные запросы (Q):       https://docs.djangoproject.com/en/5.2/topics/db/queries/#complex-lookups-with-q
Сырой SQL:                 https://docs.djangoproject.com/en/5.2/topics/db/sql/
"""

# ---------------------------------------------------------------------------
# Импорты (выполнять в оболочке: python manage.py shell)
# ---------------------------------------------------------------------------

from django.db import connection, models, reset_queries
from django.db.models import Avg, Count, Max, Min, StdDev, Sum
from django.db.models import Q
from django.db.models.functions import Abs, Power, Random

from orm_abc_app.models import AbcModel


# ===========================================================================
# 1. СОЗДАНИЕ ЗАПИСЕЙ
# ===========================================================================

# Создание объекта и сохранение в два шага
new_obj = AbcModel(task="new_task")
new_obj.save()

# Создание и сохранение за один вызов (эквивалентно)
# AbcModel.objects.create(task='new_task', a=1, b=2, c=10)


# ===========================================================================
# 2. ЧТЕНИЕ ЗАПИСЕЙ — all(), values(), values_list()
# ===========================================================================

# Все записи как QuerySet объектов AbcModel
AbcModel.objects.all()

# Итерация по QuerySet
for entry in AbcModel.objects.all():
    print(entry.task)

# Сортировка по возрастанию id с последующим разворотом
AbcModel.objects.all().order_by("id").reverse()

# values() — возвращает QuerySet словарей, а не объектов модели
AbcModel.objects.values("id", "task", "current_date").order_by("-id")

# Сложный запрос: фильтр, сортировка, срез, извлечение значения
AbcModel.objects.values().filter(id__gte=27).order_by("-id")[0:1][0]["task"]

# Получить первый/последний объект
AbcModel.objects.all().order_by("-id")[:1][0]
AbcModel.objects.values("id")[2:3]
AbcModel.objects.values()[2:4][0]["id"]

# Срез QuerySet (аналог SQL LIMIT/OFFSET)
AbcModel.objects.all()[2:4]

# values_list() — возвращает QuerySet кортежей вместо словарей
AbcModel.objects.values_list()
AbcModel.objects.values_list("id")[:1]
AbcModel.objects.values_list()[2:4][1][1]
AbcModel.objects.values_list("id", "task").order_by("id").reverse()[:3]


# ===========================================================================
# 3. УДАЛЕНИЕ ЗАПИСЕЙ — delete()
# ===========================================================================

# Удаление через фильтр
AbcModel.objects.filter(id__gte=100).delete()

# Удаление через переменную
del_obj = AbcModel.objects.filter(id__gte=100)
del_obj.delete()

# Проверка оставшихся id
AbcModel.objects.values_list("id").order_by("id").reverse()[:3]


# ===========================================================================
# 4. ОБНОВЛЕНИЕ ЗАПИСЕЙ — update()
# ===========================================================================

# Обновление одного поля
AbcModel.objects.filter(id__gte=50).update(task="updated")

# Обновление нескольких полей одновременно
update_obj = AbcModel.objects.filter(id__gte=1)
update_obj.update(task="update", b=1)

# Проверка результата
AbcModel.objects.values_list("id", "task").order_by("id").reverse()[:3]


# ===========================================================================
# 5. ОТЛАДКА SQL-ЗАПРОСОВ
# ===========================================================================

# Просмотр всех выполненных SQL-запросов (работает при DEBUG=True)
connection.queries

# Сброс истории запросов
reset_queries()


# ===========================================================================
# 6. ФИЛЬТРАЦИЯ — filter(), get(), exclude()
# ===========================================================================

# Сортировка по первичному ключу
AbcModel.objects.all().order_by("-pk")

# filter() с lookup-полями (field__lookup)
AbcModel.objects.values("pk", "b").filter(b__gte=6)  # b >= 6

# get() возвращает ровно один объект (raise исключение, если 0 или >1)
AbcModel.objects.values("pk", "b").get(pk=11)
obj = AbcModel.objects.get(pk=11)
print(obj.current_date)

# Поиск по вхождению строки (регистрозависимый)
AbcModel.objects.filter(task__contains="Ра")

# Поиск по вхождению строки (регистронезависимый — icontains)
AbcModel.objects.filter(task__icontains="Ра")

# Подсчёт результатов
AbcModel.objects.filter(task__contains="Ра").count()

# Комбинирование нескольких фильтров (логическое И через запятую)
AbcModel.objects.filter(task__icontains="на", id__gte=17)

# Пересечение двух QuerySet (оператор &)
cur_objects = (
    AbcModel.objects.filter(id__gte=17) & AbcModel.objects.filter(c__gte=15)
)

# earliest() — возвращает объект с наименьшим значением поля
cur_objects.earliest("current_date")
cur_objects.values().earliest("current_date")


# ===========================================================================
# 7. СЛОЖНЫЕ ЗАПРОСЫ — Q-объекты
# ===========================================================================

# Q-объекты позволяют строить сложные условия фильтрации
# & — логическое И,  | — логическое ИЛИ,  ~ — отрицание НЕ

# Эквивалент filter(id__gte=17, c__gte=15)
AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15))
AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values()
AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values().first()

# Пример с ИЛИ (выбрать записи, где id>=17 ИЛИ c>=15)
# AbcModel.objects.filter(Q(id__gte=17) | Q(c__gte=15))

# Пример с отрицанием (исключить записи с id>=17)
# AbcModel.objects.filter(~Q(id__gte=17))


# ===========================================================================
# 8. АГРЕГИРОВАНИЕ — aggregate(), annotate()
# ===========================================================================

cur_objects = AbcModel.objects.all()

# aggregate() — возвращает ОДИН итоговый словарь для всего QuerySet
cur_objects.aggregate(Count("id"))   # {'id__count': N}
cur_objects.aggregate(Avg("id"))     # {'id__avg': 12.5}
cur_objects.aggregate(Min("id"))     # {'id__min': 1}
cur_objects.aggregate(Max("id"))     # {'id__max': 30}
cur_objects.aggregate(StdDev("id")) # {'id__stddev': 8.3}
cur_objects.aggregate(Sum("id"))     # {'id__sum': 465}

# Именованный агрегат — можно задать своё имя ключа результата
result = cur_objects.aggregate(res=Sum("id") - Count("id"))
print(result["res"])  # доступ к значению по имени

# annotate() — добавляет вычисляемое поле к КАЖДОЙ записи QuerySet
# В отличие от aggregate(), не сворачивает в один результат
(
    AbcModel.objects.filter(id__gte=17) & AbcModel.objects.filter(c__gte=15)
).values("c").annotate(Count("id"))

# Пример: аннотировать каждую запись суммой c
r = (
    AbcModel.objects.filter(id__gte=17) & AbcModel.objects.filter(c__gte=15)
).values("c")
r.annotate(Count("c"))
r.annotate(Sum("c"))


# ===========================================================================
# 9. ФУНКЦИИ БАЗ ДАННЫХ
# ===========================================================================

# Abs() — абсолютное значение
q = AbcModel.objects.values().annotate(a1=Abs("c") + 2)
q.values("a1")
q.values("a1")[3]

# Power(base, exponent) — возведение в степень
q = AbcModel.objects.values().annotate(pw=Power("b", "c"))
q.values("b", "c", "pw")
q.aggregate(Sum("pw"))

# Random() — случайное число [0, 1) для каждой записи
res = AbcModel.objects.values().annotate(r=Random())
res.values_list("r")

# Полный список функций:
# https://docs.djangoproject.com/en/5.2/ref/models/database-functions/


# ===========================================================================
# 10. СЫРЫЕ SQL-ЗАПРОСЫ
# ===========================================================================

# raw() — выполнение произвольного SQL с маппингом на объекты модели.
# Таблица называется orm_abc_app_abcmodel (app_label + '_' + model_name).
x = AbcModel.objects.raw("SELECT * FROM orm_abc_app_abcmodel")
for obj in x:
    print(obj.id, obj.task)

# Также можно использовать connection.cursor() для полной свободы SQL:
# with connection.cursor() as cursor:
#     cursor.execute("SELECT COUNT(*) FROM orm_abc_app_abcmodel")
#     row = cursor.fetchone()
#     print(row)

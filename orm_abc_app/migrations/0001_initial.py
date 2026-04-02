# Сжатая начальная миграция для модели AbcModel.
#
# Вместо 22 исторических миграций из оригинального проекта здесь используется
# одна чистая миграция, отражающая финальное состояние модели.
#
# Это упрощает структуру проекта: новые разработчики получают одну миграцию
# вместо длинной цепочки промежуточных изменений.
#
# Для существующей базы данных с данными можно выполнить:
#     python manage.py migrate --fake-initial
#
# Сгенерировано на основе Django 5.2

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Начальная миграция: создаёт таблицу orm_abc_app_abcmodel.

    Таблица хранит записи задачи «равна ли C сумме A и B».
    """

    # Эта миграция не зависит от других (начальная)
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AbcModel",
            fields=[
                # Первичный ключ: 64-битный автоинкремент (BigAutoField)
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                # Формулировка задачи
                (
                    "task",
                    models.CharField(
                        default="Равна ли С сумме A и B?",
                        max_length=255,
                        verbose_name="Формулировка задачи",
                    ),
                ),
                # Значение A
                (
                    "a",
                    models.IntegerField(
                        default=0,
                        verbose_name="Значение А",
                    ),
                ),
                # Значение B (с подсказкой)
                (
                    "b",
                    models.IntegerField(
                        default=2,
                        help_text="Подсказка для значения B",
                        verbose_name="Значение B",
                    ),
                ),
                # Значение C (ограниченный набор choices)
                (
                    "c",
                    models.IntegerField(
                        choices=[
                            (0, "ноль"),
                            (10, "десять"),
                            (15, "пятнадцать"),
                            (20, "двадцать"),
                        ],
                        default=10,
                        verbose_name="Значение С",
                    ),
                ),
                # Результат проверки (заполняется в views.py)
                (
                    "result",
                    models.CharField(
                        default="Результат не определён",
                        max_length=255,
                        verbose_name="Результат",
                    ),
                ),
                # Дата и время последнего сохранения (auto_now)
                (
                    "current_date",
                    models.DateTimeField(
                        auto_now=True,
                        verbose_name="Дата изменения",
                    ),
                ),
            ],
            options={
                # Имена для административного интерфейса
                "verbose_name": "A_B_C Таблица",
                "verbose_name_plural": "A_B_C Таблицы",
                # Сортировка по умолчанию: новые записи первыми
                "ordering": ("-pk",),
            },
        ),
    ]

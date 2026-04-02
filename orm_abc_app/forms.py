"""
Формы приложения orm_abc_app.

Содержит два класса форм:
    AbcForm      — обычная форма Django (Form), не связана с моделью.
    AbcModelForm — форма, автоматически создаваемая из модели (ModelForm).

Документация по формам:      https://docs.djangoproject.com/en/5.2/topics/forms/
Документация по ModelForms:  https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/
Справочник по виджетам:      https://docs.djangoproject.com/en/5.2/ref/forms/widgets/
"""

from django import forms
from django.forms import ModelForm

from .models import AbcModel


class AbcForm(forms.Form):
    """
    Обычная форма Django для ввода параметров задачи A + B = C.

    Не привязана к модели — данные из неё нужно обрабатывать вручную
    (см. представление abc_get в views.py).

    Поля:
        task — текстовое поле с начальным значением (задание)
        a    — целое число A (минимум 0)
        b    — целое число B (необязательное)
        c    — целое число C с пользовательским лейблом
    """

    # CharField — строковое поле; initial задаёт значение по умолчанию
    task = forms.CharField(
        initial="Равна ли С сумме A и B?",
        label="Формулировка задачи",
    )

    # IntegerField — целочисленное поле; min_value — встроенная валидация минимума
    a = forms.IntegerField(
        initial=1,
        min_value=0,
        label="Значение А",
    )

    # required=False — поле необязательно для заполнения
    b = forms.IntegerField(
        initial=1,
        required=False,
        label="Значение B",
    )

    # label — переопределяет отображаемое название поля в форме
    c = forms.IntegerField(
        initial=1,
        label="Значение С",
    )


class AbcModelForm(ModelForm):
    """
    ModelForm для модели AbcModel.

    Django автоматически создаёт HTML-поля на основе полей модели.
    Включает встроенную валидацию типов данных и ограничений модели.

    Использование:
        form = AbcModelForm()          # пустая форма
        form = AbcModelForm(request.POST)  # форма с данными из запроса
        if form.is_valid():
            form.save()                # сохранение в БД
    """

    class Meta:
        """Настройки привязки формы к модели."""

        # Модель, на основе которой строится форма
        model = AbcModel

        # '__all__' — включить все поля модели.
        # Альтернативно можно указать явный список:
        #   fields = ['task', 'a', 'b', 'c']
        # Или исключить поля:
        #   exclude = ['result', 'current_date']
        fields = "__all__"

        # Словарь для переопределения виджетов полей.
        # Например, сделать task текстовой областью:
        # widgets = {
        #     'task': forms.Textarea(attrs={'cols': 60, 'rows': 3}),
        # }

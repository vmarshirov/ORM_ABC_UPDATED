"""
Тесты для приложения orm_abc_app.

Запуск тестов:
    python manage.py test orm_abc_app

Документация по тестированию: https://docs.djangoproject.com/en/5.2/topics/testing/
"""

from django.test import TestCase
from django.urls import reverse

from .models import AbcModel
from .views import solution


class SolutionFunctionTest(TestCase):
    """Тесты для функции solution() из views.py."""

    def test_equal(self):
        """Проверяет случай, когда C == A + B."""
        self.assertEqual(solution(2, 3, 5), "С равна сумме A и B")

    def test_not_equal(self):
        """Проверяет случай, когда C != A + B."""
        self.assertEqual(solution(1, 1, 3), "С не равна сумме A и B")

    def test_zeros(self):
        """Проверяет случай с нулями."""
        self.assertEqual(solution(0, 0, 0), "С равна сумме A и B")


class AbcModelTest(TestCase):
    """Тесты для модели AbcModel."""

    def setUp(self):
        """Создаёт тестовые данные перед каждым тестом."""
        AbcModel.objects.create(task="Тест 1", a=1, b=2, c=10)
        AbcModel.objects.create(task="Тест 2", a=5, b=5, c=10)

    def test_str_representation(self):
        """Проверяет строковое представление объекта."""
        obj = AbcModel.objects.first()
        self.assertIn(str(obj.id), str(obj))
        self.assertIn(obj.task, str(obj))

    def test_default_result(self):
        """Проверяет значение поля result по умолчанию."""
        obj = AbcModel.objects.create(task="Новая запись", a=0, b=0, c=0)
        self.assertEqual(obj.result, "Результат не определён")

    def test_ordering(self):
        """Проверяет сортировку по умолчанию (новые записи первыми)."""
        objects = AbcModel.objects.all()
        self.assertGreaterEqual(objects[0].pk, objects[1].pk)


class ViewsTest(TestCase):
    """Тесты для представлений приложения."""

    def test_index_view(self):
        """Главная страница отдаёт HTTP 200."""
        response = self.client.get(reverse("orm_abc_app:index"))
        self.assertEqual(response.status_code, 200)

    def test_abc_form_view(self):
        """Страница с формой отдаёт HTTP 200."""
        response = self.client.get(reverse("orm_abc_app:abc_form"))
        self.assertEqual(response.status_code, 200)

    def test_table_view(self):
        """Страница таблицы отдаёт HTTP 200."""
        AbcModel.objects.create(task="Тест", a=1, b=2, c=10)
        response = self.client.get(reverse("orm_abc_app:table"))
        self.assertEqual(response.status_code, 200)

"""
Вспомогательный модуль с утилитами приложения orm_abc_app.

Содержит:
    print_hi(name)      — демонстрационная функция приветствия
    solution(a, b, c)   — логика проверки равенства C = A + B

Примечание: функция solution() также присутствует в views.py, что является
намеренным дублированием для демонстрационных целей.
"""


def print_hi(name):
    """
    Выводит приветствие в стандартный вывод.

    Args:
        name (str): имя для приветствия

    Пример:
        >>> print_hi('PyCharm')
        Hi, PyCharm
    """
    print(f"Hi, {name}")


def solution(a, b, c):
    """
    Проверяет, равно ли C сумме A и B.

    Args:
        a (int): первое слагаемое
        b (int): второе слагаемое
        c (int): проверяемое значение

    Returns:
        str: строка с результатом проверки

    Примеры:
        >>> solution(1, 2, 3)
        'С равна сумме A и B'
        >>> solution(1, 2, 4)
        'С не равна сумме A и B'
    """
    if a + b == c:
        return "С равна сумме A и B"
    return "С не равна сумме A и B"


if __name__ == "__main__":
    # Точка входа при запуске файла напрямую: python print_hi.py
    print_hi("PyCharm")
    result = solution(1, 2, 3)
    print(result)

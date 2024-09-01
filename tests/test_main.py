import pytest
from main import mentors
from main import get_unique_sorted_mentor_names, analyze_mentor_names, solution


"""
Задание «Соберите уникальные имена преподавателей»
"""
def test_unique_name():
    expected = (
        'Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, '
        'Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, '
        'Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, '
        'Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
    )
    actual = get_unique_sorted_mentor_names(mentors)
    assert actual == expected


"""
Задание «Узнайте топ-3 популярных имён»
"""
# Определяем различные тестовые наборы данных для функции analyze_mentor_names
@pytest.mark.parametrize(
    "mentors, top_n, expected",
    [
        (
            # Тестовый набор 1: Стандартный случай с дубликатами имен
            [
                ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов"],
                ["Евгений Шмаргунов", "Филипп Воронов", "Олег Булыгин"],
                ["Елена Никитина", "Евгений Шек", "Дмитрий Ежков"]
            ],
            3,
            [
                ["Евгений", 3], ["Олег", 2], ["Дмитрий", 2]
            ]
        ),
        (
            # Тестовый набор 2: Случай с топ-2 именами
            [
                ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов"],
                ["Евгений Шмаргунов", "Филипп Воронов", "Олег Булыгин"],
                ["Елена Никитина", "Евгений Шек", "Денис Ежков"]
            ],
            2,
            [
                ["Евгений", 3], ["Олег", 2]
            ]
        ),
        (
            # Тестовый набор 3: Случай, где все имена уникальны
            [
                ["Иван Иванов", "Петр Петров", "Сергей Сергеев"],
                ["Анна Смирнова", "Мария Ильина", "Юлия Соколова"]
            ],
            3,
            [
                ["Иван", 1], ["Петр", 1], ["Сергей", 1]
            ]
        ),
        (
            # Тестовый набор 4: Пустой список менторов
            [],
            3,
            []
        ),
        (
            # Тестовый набор 5: Все менторы имеют одинаковое имя
            [
                ["Александр Смирнов", "Александр Иванов", "Александр Петров"],
                ["Александр Сидоров", "Александр Орлов"]
            ],
            2,
            [
                ["Александр", 5]
            ]
        )
    ]
)
def test_analyze_mentor_names(mentors, top_n, expected):
    actual = analyze_mentor_names(mentors, top_n)
    assert actual == expected


"""
Задание «Квадратное уравнение»
"""
@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 8, 15, (-3.0, -5.0)),  # Два различных корня
        (1, -13, 12, (12.0, 1.0)),  # Два различных корня
        (-4, 28, -49, 3.5),         # Один корень
        (1, 1, 1, 'корней нет'),    # Нет корней
        (1, 2, 1, -1.0),            # Один корень (d == 0)
        (0, 2, 1, None),            # Не квадратное уравнение (деление на ноль)
    ]
)
def test_solution(a, b, c, expected):
    result = solution(a, b, c)
    assert result == expected

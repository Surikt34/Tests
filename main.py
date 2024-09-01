"""
Задание «Соберите уникальные имена преподавателей»
"""
mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

def get_unique_sorted_mentor_names(mentors):
    all_list = [mentor.split()[0] for course_mentors in mentors for mentor in course_mentors]
    unique_names = sorted(set(all_list))
    all_names_sorted = ', '.join(unique_names)
    return all_names_sorted

"""
Задание «Узнайте топ-3 популярных имён»
"""


def analyze_mentor_names(mentors, top_n=3):
    """
    Объединяет все шаги анализа менторов: собирает имена, извлекает уникальные,
    подсчитывает количество вхождений и возвращает топ-N популярных имен.

    :param mentors: Список списков, содержащий имена менторов.
    :param top_n: Количество топовых имен, которые нужно вернуть.
    :return: Список топ-N имен и количество их вхождений.
    """
    # Собираем всех менторов в один список
    all_list = []
    for m in mentors:
        all_list.extend(m)

    # Извлекаем первые имена
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    # Подсчитываем количество вхождений каждого имени
    unique_names = set(all_names_list)
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    # Сортируем имена по частоте и возвращаем топ-N имен
    popular.sort(key=lambda x: x[1], reverse=True)
    return popular[:top_n]


"""
Задание «Квадратное уравнение»
"""


def discriminant(a, b, c):
    """
    Функция для вычисления дискриминанта квадратного уравнения.

    :param a: коэффициент при x^2
    :param b: коэффициент при x
    :param c: свободный член
    :return: значение дискриминанта
    """
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    Функция для нахождения корней квадратного уравнения.

    :param a: коэффициент при x^2
    :param b: коэффициент при x
    :param c: свободный член
    :return: корни уравнения (или сообщение, если корней нет)
    """
    d = discriminant(a, b, c)
    if d < 0:
        return 'корней нет'
    elif d == 0:
        x = (-b) / (2 * a)
        return x
    else:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        return x_1, x_2



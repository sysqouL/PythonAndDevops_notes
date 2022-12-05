""""""

"""
        Пример тестирования простой функции поиска. В отсортированном списке номеров, найти номер. Если он есть -
    нужно вернуть индекс, по которому он был найден. Если его нет, создать исключение типа Value Error.
        Если средний елемент равен искомому - конец. Если меньше того который ищем, то повторяем посик в левой половине списка
        Если он больше - продолжаем поиск в правой половине.
        Чтобы отслеживать область внутри списка, которую мы должны искать, сохраняем два индекса – left и right – и в каждой
    итерации перемещаем один из них ближе к другому, сокращая пространство для поиска пополам на каждом шаге.
"""

def search(needle, haystack):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        middle = left + (right - left) // 2
        middle_element = haystack[middle]
        if middle_element == needle:
            return middle
        elif middle_element < needle:
            left = middle + 1
        else:
            right = middle - 1
    raise ValueError("Value not in Haystack")

def test_search():
    assert search(2, [1,2,3,4]) == 1, 'found needle somewhere in the Haystack'

def tets_search_first_element():
    assert search(1, [1,2,3,4]) == 0, 'search first element'

def test_search_last_element():
    assert search(4, [1,2,3,4]) == 3, 'search last element'

def test_exception_not_found():
    """
    менеджер контекста pytest.raises
    метка текста в качестве именованного аргумента с именем message=
    :return:
    """
    from pytest import raises
    with raises(ValueError, message= 'left out of bounds'):
        # значение было меньше чем первый элемент списка
        search(-1, [1,2,3,4])
    with raises(ValueError, message='right out of bounds'):
        # значение было больше чем последний элемент списка
        search(5, [1,2,3,4]) #
    with raises(ValueError, message='out of bounds'):
        # значение находится между первым и последним элементом, но его просто нет в списке
        search(2, [1,3,4])
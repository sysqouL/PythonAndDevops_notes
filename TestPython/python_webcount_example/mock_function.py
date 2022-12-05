""""""

"""
    Поддельные объекты (Мок) предлагают более удобное решение. Это объекты, которые вы можете легко настроить, 
    чтобы они отвечали заранее определенным образом.
    Первые две строки этой тестовой функции импортируют класс Mock и создают из него экземпляр. Тогда происходит настоящее
    волшебство.
        mock_requests.get.return_value.text = 'aa bbb c'
    Устанавливает атрибут get в объекте mock_requests, который при его вызове возвращает другой фиктивный объект. 
    Текст атрибута этого второго фиктивного объекта имеет текст атрибута, который содержит строку 'aa bb c'.
        Давайте начнем с нескольких простых примеров. Если у вас есть объект Mock m, то m.a = 1 устанавливает атрибут 
    a со значением 1. С другой стороны, m.b.return_value = 2 настраивает m, так что m.b() возвращает 2.
    Вы можете продолжать цепочку, поэтому m.c.return_value.d.e.return_value = 3 позволяет m.c().D.e() вернуть 3. 
    По сути, каждое значение return_value в присваивании соответствует паре скобок в цепочке вызовов.

    В примере проверяется call_count поддельного объекта, который просто записывает, как часто этот ложный вызов запрашивается как функция.
    Свойство call_args содержит кортеж аргументов, переданных на его последний вызов. Первый элемент кортежа – это 
    список позиционных аргументов, второй – словарь именованных аргументов. Если вы хотите проверить несколько вызовов
    фиктивного объекта, список call_args_ содержит список таких кортежей.
"""

from unittest.mock import Mock, patch


def test_with_test_mock():
    from unittest.mock import Mock
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    result = most_common_word_in_web_page(['a', 'b', 'c'], 'https://python.org/', user_agent=mock_requests)
    assert result == 'b', 'most_common_word_in_web_page tested with test double'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] == 'https://python.org/', 'called with right URL'


def test_with_patch():
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    with patch('webcount.functions.requests', mock_requests):
        result = most_common_word_in_web_page(['a', 'b', 'c'], 'https://python.org/', )
    assert result == 'b', 'most_common_word_in_web_page tested with test double'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] == 'https://python.org/', 'called with right URL'


"""
    При вызове функции patch (импортированной из unittest.mock, стандартной библиотеки, поставляемой с Python) 
    указывается как идентификатор, который будет исправлен (временно заменен), так и тестовый двойник, которым он 
    заменяется. Функция patch возвращает менеджер контекста. Таким образом, после того как выполнение покидает блок with,
    в котором происходит вызов, временная замена отменяется автоматически.
"""
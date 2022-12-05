""""""
"""
        Эти тесты являются дополнительными примерами для модульного тестирования, и они также поднимают некоторые моменты,
    которые могут быть неочевидны при простом чтении исходного кода функции.
        most_common_word на самом деле не ищет границы слов, поэтому он с удовольствием посчитает «слово» b три раза в строке
    abbbcc.
        Функция вызовет исключение при вызове с пустым списком ключевых слов, но мы не удосужились указать, какой тип
    ошибки.
        Мы не указали, какое значение возвращать, если два или более слов имеют одинаковое количество вхождений, поэтому
    в последнем тесте использовался список из двух действительных ответов.    
"""

from python_webcount import most_common_word

def test_most_common_word():
    assert most_common_word(['a','b','c'], 'abbbcc') == 'b', 'most_common_word with unique answer'

def test_most_common_ambiguous_result():
    assert most_common_word(['a', 'b', 'c'], 'ab') in ('a', 'b'), "there might be a tie"

def test_most_common_word_empty_candidate():
    from pytest import raises
    with raises(Exception, message="empty word raises"):
        most_common_word([], 'abc')
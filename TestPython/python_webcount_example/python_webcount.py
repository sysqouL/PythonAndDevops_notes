""""""

"""
        Этот код использует библиотеку requests для извлечения содержимого веб-страницы и доступа к полученному тексту 
    (который на самом деле является HTML). Затем функция выполняет итерацию по поисковым словам, подсчитывает, как 
    часто каждое из них встречается в тексте (используя метод string.count), и создает словарь с этими подсчетами. 
    Затем он сортирует списки слов по частоте и возвращает наиболее часто встречающееся, которое является 
    последним элементом отсортированного списка.
        Функция, которая выполняет логику, most_common_word, является чистой функцией (pure function), то есть 
    возвращаемое значение зависит только от переданных ей аргументов и не имеет никаких взаимодействий 
    с внешним миром. Такая чистая функция достаточно проста для тестирования
"""

from pprint import pprint
import requests

def most_common_word(words, text):
    """
    находит наиболее распространенное слово из списка слов в фрагменте текста
    """
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]

def most_common_word_in_web_page(words, url, user_agent=requests):
    """
    user_agent=requests - необязательный аргумент, по умолчанию соответствующий библиотеке requests
    находит наиболее распространенное слово из списка слов на веб-странице, идентифицируемой по ее URL
    """
    response = user_agent.get(url)
    return most_common_word(words, response.text)

if __name__ == '__main__':
    site_url = input(str("Input site URL in format https://, example https://python.org/ -  "))
    most_common = most_common_word_in_web_page(['python ', 'Python ', 'programming '], site_url)
    print("Most common word is -", most_common)

"""
    Внедрение зависимостей:
    def test_with_test_double():
        class TestResponse():
            text = 'aa bbb c'
        class TestUserAgent():
            def get(self, url):
                self.url = url
                return TestResponse()
        test_ua = TestUserAgent()
        result = most_common_word_in_web_page(['a', 'b', 'c'],'https://python.org/',user_agent=test_ua)
        assert result == 'b', 'most_common_word_in_web_page tested with test double'
        assert test_ua.url == 'https://python.org/'
"""




#-----------------------------------------------------------------------------------------------------------------------
""""""

"""
    Пример использования argparse
"""

import argparse

if __name__ == "__main__":
    # Создаем объект для синтаксического анализатора со своим справочным сообщением
    parser = argparse.ArgumentParser(description="Echo your input")
    # Добавляем позиционно зависимую команду со своим справочным сообщением
    parser.add_argument('message', help="Message to echo")

    # Добавляем необязательный аргумент, сохраняем в виде булева значения
    parser.add_argument('--twice', '-t', help="Do it twice", action="store_true")

    # Производим синтаксический  разбор аргументов с помощью синтаксического анализатора
    args = parser.parse_args()

    print(args.message)
    if args.twice:
        print(args.message)

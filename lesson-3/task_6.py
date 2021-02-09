# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

import re


def int_func(input_string: str):

    # Решение без регулярных выражений
    # if (list(filter(lambda x: (ord(x) in range(ord('a'), ord('z')+1))
    #                 or x.isspace(), input_string))) != list(input_string):

    # Решение на regexp'ах
    p = re.compile('^[a-z\s]+$')
    if not p.match(input_string):

        print('Ошибка. Требовалось ввести строку латинских слов в нижнем регистре разделенных пробелами.')
        return

    return input_string.title()


user_input = input(
    "Введите строку латинских слов в нижнем регистре, разделенных пробелами: ")

print(f'Новая строка: {int_func(user_input)}')

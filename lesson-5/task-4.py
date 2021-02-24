# 4. Создать(не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


# Текстовый файл - см. файл "eng_numerals.txt" в текущей папке.
from sys import exit

en_ru_dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

try:
    with open("eng_numerals.txt", "r") as txtfile:

        num_list = [line.split(" — ") for line in txtfile]
        num_list = [[en_ru_dictionary[el[0]], el[1]] for el in num_list]

except:
    print('Ошибка при работе с файлом "eng_numerals.txt"')
    exit()


try:
    with open("rus_numerals.txt", "w") as txtfile:

        [txtfile.write(f'{el[0]} — {el[1]}') for el in num_list]

except:
    print('Ошибка при работе с файлом "rus_numerals.txt"')

# 5. Создать(программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
from sys import exit
from functools import reduce

try:
    with open("task-5.txt", "a") as txtfile:
        for i in range(100):
            txtfile.write(str(randint(1, 100)) + " ")

except:
    print('Ошибка при работе с файлом "task-5.txt"')
    exit()


try:
    with open("task-5.txt") as txtfile:

        result = reduce(lambda a, b: a + b,
                        [int(el) for el in [line.split(" ") for line in txtfile][0] if el])
        print(f'Сумма чисел в файле: {result}.')

except:
    print('Ошибка при работе с файлом "task-5.txt"')

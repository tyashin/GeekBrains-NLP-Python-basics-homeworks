# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

# Вариант 1
print(reduce(lambda x, y: x*y, range(100, 1001, 2)), end='\n\n')

# Вариант 2
# Примечание: пишут, что функция 'range()' не является генератором
#  (https://stackoverflow.com/questions/13092267/if-range-is-a-generator-in-python-3-3-why-can-i-not-call-next-on-a-range)
# В таком случае, следует заменить конструкцию 'range(100, 1001, 2))' на функцию-генератор.
# Это выглядит странно, но соответствует условию задачи.


def generate_even_nums(start, finish):
    for num in range(start, finish, 2):
        yield num


print(reduce(lambda x, y: x*y, generate_even_nums(100, 1001)))

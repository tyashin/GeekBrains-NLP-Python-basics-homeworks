# 1. Реализовать функцию, принимающую два числа(позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def divide(dividend, divisor):

    if not isinstance(dividend, (float, int)) or not isinstance(divisor, (float, int)):
        print('Переданные аргументы должны быть числового типа')
        return

    elif divisor == 0:
        print('Делитель должен быть не равен 0')
        return

    return dividend/divisor


dividend = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))

print(f"Результат деления { divide(dividend, divisor) }")

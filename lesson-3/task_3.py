# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):

    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)) or not isinstance(c, (float, int)):
        print('Переданные аргументы должны быть числового типа')
        return

    args = [a, b, c]
    args.sort(reverse=True)
    return args[0] + args[1]


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(my_func(a, b, c))

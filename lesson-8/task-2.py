"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве 
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class ZeroDivisionErrorPlus(Exception):
    def __init__(self, error_message):
        self.txt = error_message


for _ in range(1, 5):
    divider = int(input('Введите значение делителя: '))

    try:
        if divider == 0:
            raise ZeroDivisionErrorPlus(
                "Вам пока не разрешено делить на ноль.")
    except ZeroDivisionErrorPlus as e:
        print(e.txt)
    else:
        print(f'100 / {divider} = {100/divider}')

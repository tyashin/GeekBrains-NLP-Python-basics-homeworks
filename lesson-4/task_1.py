# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv, exit

script_name, production, h_rate, bonus = argv

try:
    production = float(production)
    h_rate = float(h_rate)
    bonus = float(bonus)
except:
    print('Неверный ввод!')
    exit()

if min(production, h_rate, bonus) < 0:
    print('Значения выработки, часовой ставки и премии должны быть больше 0!')
    exit()


print(f'Результат расчета: {round((production *h_rate)+bonus, 2)}')

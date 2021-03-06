# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

import sys

seasons_list = ['Зима']*2 + ['Весна']*3 + ['Лето']*3 + ['Осень']*3 + ['Зима']
seasons_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
                6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}


month_num = int(input('Введите номер месяца 1-12: '))

if month_num < 1 or month_num > 12:
    print('Ошибка ввода')
    sys.exit()

print(f"Выбранное время года - {seasons_list[month_num-1]}.")
print(
    f"Мы еще раз проверили и подтверждаем: выбранное время года - {seasons_dict[month_num]}.")

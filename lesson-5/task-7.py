"""7. Создать(не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""

# Текстовый файл - см. "task-7.txt" в текущей папке.
import json
from sys import exit

profits_dict = {}
firms_num = 0
total_profit = 0

try:
    with open("task-7.txt") as txtfile:
        for line in txtfile:
            firms_list = line.split(" ")
            current_profit = int(
                firms_list[2].strip()) - int(firms_list[3].strip())

            profits_dict[firms_list[0].strip()] = current_profit

            if current_profit > 0:
                total_profit += current_profit
                firms_num += 1

        avg_profit_dict = {'average profit': round(
            total_profit/firms_num if firms_num > 0 else 0, 0)}

        result_list = [profits_dict, avg_profit_dict]
        print(f'Результат: {result_list}')

except:
    print('Ошибка при работе с файлом "task-7.txt"')
    exit()


try:
    with open('json_analytics.json', 'w') as json_file:
        json.dump(result_list, json_file)

except:
    print('Ошибка при работе с файлом "json_analytics.json"')

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами(характеристиками
# товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [

#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {“название”: [“компьютер”, “принтер”, “сканер”],
#  “цена”: [20000, 6000, 2000],
#  “количество”: [5, 2, 7],
#  “ед”: [“шт.”]

#  }

import sys

goods = []


def add_edit_goods():
    try:
        product_id = int(input('Введите числовой код товара: '))
        product_name = (input('Введите название товара: ')).strip()
        product_price = float(input('Введите цену товара: '))
        product_amount = int(
            float(input('Введите количество товара: ')))
        product_units = (input('Введите единицу измерения товара: ')).strip()

        existing_product = search(product_id)

        if existing_product:
            goods.remove(existing_product)

        goods.append((product_id, {
            'название': product_name, 'цена': product_price, 'количество': product_amount, 'ед': product_units}))
        print('Информация о товаре добавлена.')
        return

    except:
        print('Ошибка ввода!')
        return


def show_analytics():
    analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
    for el in goods:
        analytics['название'].append(el[1]['название'])
        analytics['цена'].append(el[1]['цена'])
        analytics['количество'].append(el[1]['количество'])
        analytics['ед'].append(el[1]['ед'])

    analytics['ед'] = list(set(analytics['ед']))
    print(analytics)


def show_goods():
    for el in goods:
        print(f"Код товара: {el[0]}", end=', ')
        for key, value in el[1].items():
            print(f"{key} : {value}", end=', ')
        print()


def search(product_id):
    for el in goods:
        if el[0] == product_id:
            return el
    return None


switcher = {1: show_goods, 2: add_edit_goods, 3: show_analytics, 0: sys.exit}

print('Программа "Нано-складской учет"')

while True:
    choice = int(input(
        'Опции: Просмотр данных о товарах - "1"; Ввод/редактирование данных о товарах - "2"; Просмотр аналитики - "3"; Выход из программы - "0": '))

    if choice not in [0, 1, 2, 3]:
        print('Неверный ввод')
        continue

    switcher[choice]()

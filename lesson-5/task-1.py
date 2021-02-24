# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('user_data', 'a') as text_file:
    while True:
        input_str = (input(
            'Введите строку символов, для завершения ввода введите пустую строку:')).strip()
        print(input_str)

        if not input_str:
            break
        else:
            text_file.write(input_str+'\n')

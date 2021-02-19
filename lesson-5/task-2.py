# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# Текстовый файл - см. "task-2-text-file.txt" в текущей папке.

with open("task-2-text-file.txt") as txtfile:

    result = [len(line.split()) for line in txtfile]
    print(f'Количество строк: {len(result)}.')

    [print(f'В строке {ind+1} - {el} слов(а).')
     for ind, el in enumerate(result)]

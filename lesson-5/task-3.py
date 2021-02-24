# 3. Создать текстовый файл(не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


# Текстовый файл - см. файл "salaries.txt" в текущей папке.

wage_fund = 0
empl_num = 0

print('Список сотрудников с окладом < 20000:')

try:
    with open("salaries.txt", "r") as txtfile:

        for line in txtfile:
            list = line.split(",")
            surname, salary = list
            salary = int(salary.strip())
            wage_fund += salary
            empl_num += 1

            if salary < 20000:
                print(f'У сотрудника (-цы) {surname} оклад = {salary}')

        if empl_num:
            print(
                f'Средняя величина дохода сотрудниов: {round(wage_fund / empl_num, 2) }')
except:
    print('Ошибка при работе с файлом')

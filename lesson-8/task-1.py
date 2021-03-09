"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки 
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @ classmethod, 
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, 
с декоратором @ staticmethod, должен проводить валидацию числа, месяца и года(например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных."""


class Date():

    def __init__(self, date_string):
        self.date, self.month, self.year = Date.convert_date_elements_to_int(
            date_string)

    def __str__(self):
        return (f'{self.date}-{self.month}-{self.year}' if self.date != None else 'None')

    @classmethod
    def convert_date_elements_to_int(cls, date_string):

        try:
            date_elements = date_string.split('-')
            if len(date_elements) != 3:
                raise Exception
            date_elements = [int(el) for el in date_elements]
            date_elements = Date.validate_date(date_elements)
        except:
            return [None, None, None]

        return date_elements

    @staticmethod
    def validate_date(date_elements):

        try:
            if not date_elements[1] in range(1, 13):
                raise Exception
            elif not date_elements[0] in range(1, Date.number_of_days_in_a_month(date_elements[2], date_elements[1])+1):
                raise Exception
            return date_elements
        except:
            return [None, None, None]

    @staticmethod
    def number_of_days_in_a_month(y, m):
        leap = 0
        if y % 400 == 0:
            leap = 1
        elif y % 100 == 0:
            leap = 0
        elif y % 4 == 0:
            leap = 1
        if m == 2:
            return 28 + leap
        list = [1, 3, 5, 7, 8, 10, 12]
        if m in list:
            return 31
        return 30


print(Date('26-3-2021'))
print(Date('29-2-2021'))   # Ошибка
print(Date('30-18-2021'))  # Ошибка

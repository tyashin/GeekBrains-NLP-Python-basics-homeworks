"""1. Реализовать класс Matrix(матрица). Обеспечить перегрузку конструктора класса(метод __init__()),
который должен принимать данные(список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:

    def __init__(self, m_data):

        self.matrix = m_data

    def __str__(self):

        result = ''

        for m_string in self.matrix:
            m_string_result = ''
            for m_col in m_string:
                m_string_result += '{0: <6}'.format(str(m_col))
            result += m_string_result + '\n'

        return result

    def __add__(self, other):

        try:
            new_m_data = self.matrix.copy()

            for m_string in range(0, len(self.matrix)):
                for m_col in range(0, len(self.matrix[m_string])):

                    new_m_data[m_string][m_col] += other.matrix[m_string][m_col]

            return(Matrix(new_m_data))

        except:
            print('Складывать можно только матрицы одинакового размера!')


matrix = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [
    13, 14, 15, 16], [17, 18, 19, 20]])
print(f'Первая матрица: ' + '\n' + str(matrix))

second_matrix = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [
                       1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(f'Вторая матрица: ' + '\n' + str(second_matrix))

print(f'Результирующая матрица: ' + '\n' + str(matrix + second_matrix))

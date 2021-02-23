"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность(класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
размер(для пальто) и рост(для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто(V/6.5 + 0.5), 
для костюма(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @ property."""

from abc import ABC, abstractmethod


class Clothing(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material_consumption(self):
        pass


class Costume(Clothing):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def material_consumption(self):
        return round(2 * self.height + 0.3, 2)


class Coat(Clothing):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def material_consumption(self):
        return round(self.size/6.5 + 0.5, 2)


coat = Coat('Демисезонное', 50)
costume = Costume('Смокинг', 1.7)

print(f'Расход ткани на {coat.name} пальто: {coat.material_consumption}')
print(
    f'Расход ткани на {costume.name}: {costume.material_consumption}')

print(
    f'Суммарный расход ткани : {round(coat.material_consumption + costume.material_consumption, 2)}')

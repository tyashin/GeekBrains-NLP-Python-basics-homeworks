"""5. Реализовать класс Stationery(канцелярская принадлежность). 
Определить в нем атрибут title(название) и метод draw(отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen(ручка), 
Pencil(карандаш), Handle(маркер). В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры 
классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen (Stationery):

    def draw(self):

        # Нарушаем DRY principle, т.к. это требуется по условию.
        print(f'Объект для рисования: {self.title}')


class Pencil (Stationery):

    def draw(self):
        print(f'Объект для рисования: {self.title}')


class Handle (Stationery):

    def draw(self):
        print(f'Объект для рисования: {self.title}')


list = []
list.append(Stationery('Канцелярка'))
list.append(Pen('Ручка'))
list.append(Pencil('Карандаш'))
list.append(Handle('Маркер'))

[el.draw() for el in list]

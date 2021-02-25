"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
name, is_police(булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула(куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

from random import randint


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = {1: "лево", 2: "право"}

    def go(self):
        print('Машина тронулась')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{self.direction[direction]}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы превысили скорость!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость!')

        super().show_speed()


car_list = []
car_list.append(TownCar(80, 'зеленый', 'Лада', False))
car_list.append(SportCar(150, 'красный', 'Ferrari', False))
car_list.append(PoliceCar(100, 'голубой', 'Москвич', True))
car_list.append(WorkCar(60, 'серый', 'ЗИС', False))

for el in car_list:
    print(f'Модель: {el.name}')
    print(f'Цвет: {el.color}')
    el.show_speed()
    print(f'Это полицейское авто: {el.is_police}')
    el.turn(randint(1, 2))
    el.stop()
    print()

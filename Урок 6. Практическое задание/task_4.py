"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import self as self


class Car:
    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} стоит')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')

class TownCar(Car):
    def show_speed(self):
        lim = 60
        if self.speed <= lim:
            print(f'{self.name} едет со скоростью {self.speed}')
        else:
            print(f'{self.name} едет с превышением установленной скорости {lim}')


class WorkCar(Car):
    def show_speed(self):
        lim = 40
        if self.speed <= lim:
            print(f'{self.name} едет со скоростью {self.speed}')
        else:
            print(f'{self.name} едет с превышением установленной скорости {lim}')


class SportCar(Car):
    pass

class PoliceCar(Car):
    pass


a = WorkCar(70, 'red', 'WorkCar', False)
print(a.name, a.color)
a.show_speed()

b = SportCar(60, 'green', 'SportCar', False)
print(b.name, b.color)
b.show_speed()
b.turn('left')

c = TownCar(60, 'black', 'TownCar', False)
print(c.name, c.color)
c.show_speed()

d = PoliceCar(60, 'black', 'TownCar', True)
print(d.name, d.color)
d.go()
d.show_speed()

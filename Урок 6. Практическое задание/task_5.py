"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        n = 'Ручка'
        print(f'Запуск отрисовки с помощью {n}')

class Pencil(Stationery):
    def draw(self):
        n = 'Карандаш'
        print(f'Запуск отрисовки с помощью {n}')

class Handle(Stationery):
    def draw(self):
        n = 'Маркер'
        print(f'Запуск отрисовки с помощью {n}')


a = Pen('Pen')
b = Pencil('Pen')
c = Handle('Pen')
d = Stationery('Stationery')

a.draw()
b.draw()
c.draw()
d.draw()

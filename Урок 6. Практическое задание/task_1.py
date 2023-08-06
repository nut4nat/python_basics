"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


class TrafficLight:
    __color = ('red', 'yellow', 'green')

    def running(self):
        import time
        i = 0
        period = (7, 2, 5)
        while True:
            print(self.__color[i])
            time.sleep(period[i])
            i = i + 1
            if i > len(period)-1:
                break

obj = TrafficLight()
obj.running()

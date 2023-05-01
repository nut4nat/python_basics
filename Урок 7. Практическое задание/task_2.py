"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class General(ABC):
    @abstractmethod
    def fabric_demand(self):
        pass


class Clothes(General):
    def __init__(self, cl_type, param: int):
        self.cl_type = cl_type
        self.param = param
        self._demand = 0

    @property
    def fabric_demand(self):
        if self.cl_type == 'coat':
            self._demand = round(self.param / 6.5 + 0.5)
            return f'Расход ткани на пальто: {self._demand} ед.'
        elif self.cl_type == 'suit':
            self._demand = round(2 * self.param + 0.3)
            return f'Расход ткани на костюм: {self._demand} ед.'

    def __call__(self):
        return int(self._demand)

example1 = Clothes('coat', 44)
example2 = Clothes('suit', 60)
print(example1.fabric_demand)
print(example2.fabric_demand)
print(f'Общий расход ткани {example1()+example2()} ед.')

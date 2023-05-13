"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

from datetime import datetime


class Data:
    day = 0
    month = 0
    year = 0

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def get_data(cls, day_month_year):
        lst = day_month_year.split('_')
        Data.day = int(lst[0])
        Data.month = int(lst[1])
        Data.year = int(lst[2])
        print(f'{Data.day}, {Data.month}, {Data.year}')

    @staticmethod
    def validate_get_data():
        if 0 < Data.year <= datetime.now().year:
            if 0 < Data.month <= 12:
                if 0 < Data.day <= 31:
                    print(f'Валидная дата')
                else:
                    print(f'Невалидный day')
            else:
                print(f'Невалидный month')
        else:
            print(f'Невалидный year')


a = Data(10_11_2024)
a.get_data('10_11_2024')
a.validate_get_data()

Data.get_data('10_11_2019')
Data.validate_get_data()

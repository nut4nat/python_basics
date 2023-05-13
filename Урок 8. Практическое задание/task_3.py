"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotNumError(Exception):
    def __init__(self, txt):
        self.txt = txt


lst = []

while True:
    try:
        a = input('Input number for the List: ')
        if a == '!':
            break
        if not a.isdigit():
            raise NotNumError('it is not number! Try again to input number!')
    except NotNumError as err:
        print(err)
    else:
        lst.append(int(a))
    finally:
        print(f'Input ! to finish. Current List: {lst}')

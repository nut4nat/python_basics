"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

my_list = [None, False, 100, 1.1, -2, 'abra']
for i in range(len(my_list)):
    print(type(my_list[i]))

my_list = [None, False, 100, 1.1, -2, 'abra']
for el in my_list):
    print(type(el))

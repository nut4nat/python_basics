"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

def divide(num1, num2):
    """
    Делит num1 на num2 и возвращает число
    При обнаружении 0 в делителе возращает текст Ошибки
    """
    try:
        result = num1/num2
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')
    return result

n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
print(divide(n1, n2))

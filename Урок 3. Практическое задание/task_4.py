"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def exponent(x, y):
    """Возведение в отрицательную степень с помощью **"""
    result = x ** y
    return result
    except TypeError:

def exponent2(x, y):
    """
    Возведение в отрицательную степень с помощью формулы x(-y) = 1/x(y),
    где y - абсолютное значение отрицательной степени -n"""
    divider = 1
    for i in range(abs(y)):
        divider = divider*x
    result = 1/divider
    return result

print(exponent(2, -3))
print(exponent2(2, -3))

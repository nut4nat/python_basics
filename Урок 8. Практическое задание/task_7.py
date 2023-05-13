"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:
    # Комплексное число состоит из действительной и мнимой частей
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + {self.imaginary}*i'

    def __add__(self, other):
        # ( a + b i ) + ( c + d i ) = ( a + c ) + ( b + d ) i
        res_real = self.real + other.real
        res_imaginary = self.imaginary + other.imaginary
        return f'Сложение: {ComplexNum(res_real, res_imaginary)}'

    def __mul__(self, other):
        # (a + b i ) (c + d i ) = a c + a d i + b c i + b d i 2
        res_real = self.real * other.real + self.imaginary * other.imaginary # i в четной степени = 1 -> переносим в действительную часть
        res_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return f'Умножение: {ComplexNum(res_real, res_imaginary)}'

a = ComplexNum(4, 5)
b = ComplexNum(3, 2)
print(a)
print(b)
print(a + b)
print(a * b)

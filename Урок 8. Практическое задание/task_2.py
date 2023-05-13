"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DividerError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = int(input('Input dividend: '))
divider = int(input('Input divider: '))

try:
    if divider == 0:
        raise DividerError('Divider should not be 0!')
except DividerError as err:
    print(err)
else:
    div = dividend/divider
    print(f'Result of dividing = {div}')

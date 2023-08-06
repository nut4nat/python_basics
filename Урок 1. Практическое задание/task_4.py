"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
number = int(input("Input integer figure>>>"))

last_figure = number % 10  # получаем остаток от деления - последнюю цифру в числе
number = number // 10  # получаем число без последней цифры

while number > 9:
    prelast_figure = number % 10
    if prelast_figure > last_figure:
        last_figure = prelast_figure
    number = number // 10
else:
    if last_figure >= number:
        print(last_figure)
    else:
        print(number)

"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 1]

val = int(input('Введите новое натуральное число>>>'))
my_list.append(val)

# последовательное сравнение последнего элемента с предыдущим
for i in range(len(my_list)-1, 0, -1):
    if my_list[i] > my_list[i-1]:
        my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(f'Пользователь ввел число {val}. Результат: {my_list}')

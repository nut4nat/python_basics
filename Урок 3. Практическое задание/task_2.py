"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_person_data(*data):
    print(f'{data[0]} {data[1]} {data[2]} года рождения, проживает в городе {data[3]}, email: {data[4]}, телефон: {data[5]}')

print_person_data('Ann', 'Black', '1988', 'Moscow', 'no', '1111')

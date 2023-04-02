"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_in_sec = int(input("Input time in seconds >>>"))

hour = time_in_sec // 3600
minute = (time_in_sec % 3600) // 60
second = (time_in_sec % 3600) % 60
print(f"This time in format hh:mm:ss = {hour}:{minute}:{second}")
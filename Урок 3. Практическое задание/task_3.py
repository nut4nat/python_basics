"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(*nums):
    s_tuple = sorted(nums)
    return s_tuple[len(s_tuple)-1]*s_tuple[len(s_tuple)-2]

print(my_func(1,7,3))

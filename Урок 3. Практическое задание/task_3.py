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

def my_func2(*nums):
    my_list = list(nums)
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list[len(my_list)-1] * my_list[len(my_list)-2]

print(my_func(1, 7, 3))
print(my_func2(1, 7, 3))

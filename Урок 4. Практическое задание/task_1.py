 """
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

def salary(hrs, hrpay, bonus):
    return (int(hrs) * int(hrpay)) + int(bonus)

task_1, num1, num2, num3 = argv
print (f'Заработная плата = {salary(num1, num2, num3)}')

"""
PS C:\Users\Nata\Desktop\Python_Basics_GIT>  python task_1.py 1 1 1
Заработная плата = 2
"""

"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


f_obj = open("new_f.txt", 'a')

while True:
    string = input("введите строку для записи>>>")
    len(string) > 0
    f_obj.writelines(string+'\n')

    if not string:
        break

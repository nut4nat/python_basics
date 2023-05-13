"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# Открытие файла и запись строк
f = open("my_file.txt", 'w')
str_list = ['abra cadabra\n', 'abra\n', 'cadabra\n']
f.writelines(str_list)
f.close()

# Подсчет количества строк и слов в каждой строке
f = open('my_file.txt')
str_list = f.readlines()
print(f'Количество строк: {len(str_list)}')

with open("my_file.txt") as f:
    for line in f:
        print(f'Количество слов в строке ({line}): {len(line.split())}')

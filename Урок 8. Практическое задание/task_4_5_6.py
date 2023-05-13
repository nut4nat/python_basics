"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class NotPositiveNum(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.dpt = []  # отделы ['accountant', 'sales', 'administration']
        self.inhouse = {}  # Наименование и кол-во хранится на складе
        self.given = {i: {} for i in self.dpt}  # Наименование и кол-во передано со склада в отдел

    def __str__(self):
        return f'На складе имеется: {self.inhouse}'

    def send_to_wh(self, item, qty):
        """
        Метод отправляет в словарь склада inhouse указанный item и его количество qty
        :type qty: int
        """
        try:
            if qty < 0:
                raise NotPositiveNum('Negative number! Try again to input Positive number!')
        except NotPositiveNum as err:
            print(err)
        else:
            if item in self.inhouse:
                self.inhouse[item] += qty
                print(f'{item} в количестве {qty} добавлен на склад')
            else:
                self.inhouse[item] = qty
                print(f'{item} в количестве {qty} добавлен на склад')

    def get_from_wh(self, item, qty, dpt):
        """
        Метод получает из словаря склада inhouse указанный item и его количество qty и перемещает в словарь выдачи given для указанного отдела dpt
        :type qty: int
        """
        try:
            if qty < 0:
                raise NotPositiveNum('Negative number! Try again to input Positive number!')
        except NotPositiveNum as err:
            print(err)
        else:
            if item in self.inhouse:
                if qty <= self.inhouse[item]:
                    self.inhouse[item] -= qty  # Списание из inhouse
                    if dpt in self.given:  # Добавление в given c поиском dpt
                        if item in self.given[dpt]:
                            self.given[dpt][item] += qty
                        else:
                            self.given[dpt][item] = qty
                            print(f'{item} в количестве {qty} выдан со склада в {dpt}')
                    else:
                        self.given[dpt] = {item: qty}
                        print(f'{item} в количестве {qty} выдан со склада в {dpt}')
                else:
                    print(f'Нет нужного количества {item} на складе')
            else:
                print(f'Не найдено {item} на складе')


class Orgtechnic:
    type_lst = ['printer', 'scanner', 'xerox']
    cond_lst = ['defective', 'active', 'obsolete']

    def __init__(self, type, condition):
        self.type = self._is_valid_type(type)
        self.condition = self._is_valid_condition(condition)

    def _is_valid_type(self, type):
        if type not in Orgtechnic.type_lst:
            raise ValueError("Unexpectable type")
        return type

    def _is_valid_condition(self, condition):
        if condition not in Orgtechnic.cond_lst:
            raise ValueError("Unexpectable condition")
        return condition


class Printer(Orgtechnic):
    def __init__(self, type, condition, color: bool):
        super().__init__(type, condition)
        self.color = color  # [чб или цветной]


class Scanner(Orgtechnic):
    pass


class Xerox(Orgtechnic):
    pass


a = Warehouse()
print(a)

p = Printer('printer', 'defective', True)
s = Scanner('scanner', 'active')

a.send_to_wh(p.type, 2)
print(a)
a.send_to_wh(s.type, -1)
print(a)
a.get_from_wh(p.type, 1, 'sales')
print(a.given)
a.get_from_wh(s.type, 8, 'sales')
print(a.given)

x = Xerox('xeroxX', 'active')

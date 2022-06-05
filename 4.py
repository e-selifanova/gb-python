"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Stock:
    stock = {}


class OfficeEquipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    laser: bool

    def __init__(self, name, price, laser=True):
        super().__init__(name, price)
        self.laser = laser


class Scanner(OfficeEquipment):
    manual: bool

    def __init__(self, name, price, manual=True):
        super().__init__(name, price)
        self.manual = manual


class Copier(OfficeEquipment):
    colored: bool

    def __init__(self, name, price, colored=True):
        super().__init__(name, price)
        self.colored = colored


"""
5. Продолжить работу над первым заданием (которое наверное 4). Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""


class Stock:
    stock = {}
    departments = {}

    def add_stock(self, item, count):
        self.stock[item] += count

    def move_department(self, item, count, department):
        self.stock[item] -= count
        if item in self.departments[department].keys():
            self.departments[department][item] += count
        else:
            self.departments[department][item] = count


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

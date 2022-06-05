"""
6. Продолжить работу над вторым заданием (которое видимо 5). Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Stock:
    stock = {}
    departments = {}

    def __init__(self, department: tuple):
        self.stock = {}
        for i in department:
            if type(i) != str:
                self.departments = {}
                print('Необходимо передать список подразделений!')
                return
            self.departments[i] = {}

    def add_stock(self, item, count):
        if not isinstance(item, (Printer, Scanner, Copier)):
            print(f'Нет такого типа оргтехники!({item})')
            return
        if type(count) != int or count <= 0:
            print('Количество оргтехники должно быть больше 0')
            return
        self.stock[item] += count

    def move_department(self, item, count, department):
        if not isinstance(item, (Printer, Scanner, Copier)):
            print(f'Попытка перемещения не существующего типа оргтехники({item})!')
            return
        if type(count) != int or count <= 0:
            print('Количество оргтехники должно быть больше 0')
            return
        if self.stock[item] - count < 0:
            print(f'Запрошенного количества оргтехники {item} нет на складе')
            return
        self.stock[item] -= count
        if item in self.departments[department].keys():
            self.departments[department][item] += count
        else:
            self.departments[department][item] = count

    def add_model(self, model):
        self.stock[model] = 0

    def __repr__(self):
        return str(self.stock) + '\n' + str(self.departments)


class OfficeEquipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '\n' + self.__class__.__name__ \
               + ': ' + str(self.__dict__)


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


def test_usage():
    stock = Stock(('Отдел эксплуатации', 'Отдел Мониторинга', 'Отдел RnD'))

    printer1 = Printer('printer1', 1000, laser=True)
    scanner1 = Scanner('scanner1', 2000, manual=False)
    copier1 = Copier('copier1', 3000, colored=True)

    stock.add_model(printer1)
    stock.add_model(scanner1)
    stock.add_model(copier1)

    print(f'Остатки оргтехники: {stock}')

    stock.add_stock(printer1, 20)
    stock.add_stock(scanner1, 10)
    stock.add_stock(copier1, 2)

    print(f'Остатки оргтехники: {stock}')

    stock.move_department(printer1, 5, 'Отдел RnD')

    stock.move_department(printer1, 5, 'Отдел эксплуатации')
    stock.move_department(scanner1, 5, 'Отдел Мониторинга')
    stock.move_department(copier1, 2, 'Отдел RnD')

    print(f'Остатки оргтехники: {stock}')

    stock.move_department(printer1, 10, 'Отдел эксплуатации')
    stock.move_department(scanner1, 5, 'Отдел Мониторинга')
    stock.move_department(copier1, 3, 'Отдел RnD')

    print(f'Остатки оргтехники: {stock}')


if __name__ == '__main__':
    test_usage()

"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def to_int(cls, data):
        d, m, y = data.split('-')
        return cls(int(d), int(m), int(y))

    @staticmethod
    def validdate(obj):
        if obj.day < 1 or obj.day > 31:
            return f"Неверно введен день {obj.day} (диапазон 1-31)"
        elif obj.month > 12 or obj.month < 1:
            return f"Неверно введен месяц {obj.month} (диапазон 1-12)"
        elif obj.year < 1 or obj.year > 9999:
            return f"Неверно введен год {obj.year} (диапазон 1-9999)"
        else:
            return f"{obj.day}-{obj.month}-{obj.year}"


test_date = Data.to_int("07-08-1986")
print(Data.validdate(test_date))

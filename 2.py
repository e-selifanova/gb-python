"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class DivZero(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = float(input('Введите первое число:'))
    b = float(input('Введите второе число:'))
    if b == 0:
        raise DivZero('Деление на ноль!!!')
    print(a / b)
except DivZero as inc:
    print(inc)

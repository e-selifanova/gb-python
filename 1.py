'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

# пример списка из передаваемых аргументов ['./1.py', '3.5', '4.5', '500']
file_name, worked_hour, rate, benefit = argv

print(argv)

salary = (float(worked_hour) * float(rate)) + float(benefit)
print(f"Ваша зарплата составляет: {salary}")


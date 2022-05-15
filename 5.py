'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randrange

with open("task5.txt", "w") as file_object:
    for i in range(10):
        file_object.write(str(randrange(1, 10)) + " ")

with open('task5.txt', 'r') as file_object:
    my_line = file_object.readline().split()
    total = sum([int(el) for el in my_line])
    print(f"Сумма равна: {total}")

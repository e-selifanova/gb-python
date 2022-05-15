'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

translate_list = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

with open('task4.txt', 'r') as file_object:
    for i in file_object:
        i = i.split(' ', 1)
        new_file.append(translate_list[i[0]] + '  ' + i[1])

with open('task4_new.txt', 'w') as file_object:
    file_object.writelines(new_file)

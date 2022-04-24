# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

created_list = [66, -66, 66.6, True, False, "String"]

# Простой цикл
for i in range(len(created_list)):
    print(type(created_list[i]))

# С использованием функции
def get_type(created_list):
    for i in range(len(created_list)):
        print(type(created_list[i]))
    return
get_type(created_list)


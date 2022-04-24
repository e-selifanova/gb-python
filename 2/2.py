# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

created_list = []
count = int(input("Количество элементов списка:"))

i = 0
while i < count:
    created_list.append(input("Значение %d элемента списка:" %i))
    i += 1

j = 0
for k in range(int(len(created_list)/2)):
        created_list[j], created_list[j + 1] = created_list[j + 1], created_list[j]
        j += 2
print(created_list)


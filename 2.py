'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

with open("task2.txt") as file_object:
    lines = 0
    letters = 0
    for line in file_object:
        letters = len(line.split())
        print(f"Всего слов в {lines + 1} строке: {letters}")
        lines += 1

print(f"Всего строк: {lines}")

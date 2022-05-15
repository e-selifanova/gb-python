'''
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
'''

import json

i = 0
profit = 0
result = {}
average_profit = {}

with open("task7.txt", 'r') as file_object:
    for line in file_object:
        name, form, revenue, costs = line.split(" ")
        if int(revenue) > int(costs):
            result[name] = int(revenue) - int(costs)
            profit += int(revenue) - int(costs)
            i += 1
        else:
            result[name] = int(revenue) - int(costs)
average_profit["average_profit: "] = profit / i
result = [result, average_profit]

with open("task7.json", "w")  as file_object:
    json.dump(result, file_object, ensure_ascii=False)

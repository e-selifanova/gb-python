# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк. 3610

import time

print("Введите время в секундах: ")
a = int(input())

result_time = time.gmtime(a)
format_time = time.strftime("%H:%M:%S",result_time)

print(format_time)



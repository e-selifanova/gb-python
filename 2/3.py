# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

year_time_list = ['зима', 'весна', 'лето', 'осень']
year_time_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}

get_month = int(input("Введите номер месяца:"))

if get_month == 1 or get_month == 12 or get_month == 2:
    print(year_time_dict.get(1))
    print(year_time_list[0])
elif get_month == 3 or get_month == 4 or get_month ==5:
    print(year_time_dict.get(2))
    print(year_time_list[1])
elif get_month == 6 or get_month == 7 or get_month == 8:
    print(year_time_dict.get(3))
    print(year_time_list[2])
elif get_month == 9 or get_month == 10 or get_month == 11:
    print(year_time_dict.get(4))
    print(year_time_list[3])
else:
    print("Вы ввели некорректный номер месяца %d!" %get_month)

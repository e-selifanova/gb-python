# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print("Введите число n: ")
n = int(input())

sec_oper = str(n) * 2
third_oper = str(n) * 3

print(n + int(sec_oper) + int(third_oper))


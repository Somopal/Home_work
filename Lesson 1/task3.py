"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, # пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
n = input("Введите число n от 0 до 9, n =  ")
# n + nn + nnn = n + 11n + 111n = 123n
res = int (n) * 123
print(f'сумма чисел  {int(n)} + {int(n * 2)} + {int(n * 3)} = {res}')
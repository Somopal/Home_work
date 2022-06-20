"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к
какому времени года относится месяц (зима, весна, лето, осень). Напишите
решения через list и dict.
"""
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
mon = int(input("Введите месяц по номеру "))
if mon == 12 or mon == 1 or mon == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif mon == 3 or mon == 4 or mon == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif mon == 6 or mon == 7 or mon == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif mon == 9 or mon == 10 or mon == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

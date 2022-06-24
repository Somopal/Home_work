"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    new_list = [arg_1, arg_2, arg_3]
    new_list.remove(min(arg_1, arg_2, arg_3))
    return sum(new_list)


num_1, num_2, num_3 = int(input("Введите первое число: ")), int(
    input("Введите второе число: ")), int(input("Введите третье число: "))

print(my_func(num_1, num_2, num_3))

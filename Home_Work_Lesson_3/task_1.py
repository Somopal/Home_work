"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""


def my_division(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        exit()


first_numb = int(input("Введите первое число: "))
second_numb = int(input("Введите второе число: "))

print(f'{first_numb} : {second_numb} = {my_division(first_numb, second_numb)}')

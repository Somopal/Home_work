"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать
функцию type() для проверки типа. Элементы списка можно не запрашивать у
пользователя, а указать явно, в программе.
"""
my_list = ['Привет', 818, None, False, 4.50]
for el in my_list:
    print('element: ', el, '\ntype: ', type(el))
    print('')
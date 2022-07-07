"""
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите
условие его завершения. #### Например, в первом задании выводим целые числа,
начиная с 3. При достижении числа 10 — завершаем цикл. Вторым пунктом
необходимо предусмотреть условие, при котором повторение элементов списка
прекратится.
"""
from itertools import count, cycle

start, finish = int(input('Укажите первое число последовательности: ')), int(
    input('Укажите последнее число последовательности: '))
for number in count(start):
    if number <= finish:
        print(number)
    else:
        break

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
i = 0
for item in cycle(lst):
    if i < len(lst):
        print(item)
        i += 1
    else:
        break
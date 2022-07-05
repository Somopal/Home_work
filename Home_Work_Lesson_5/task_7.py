"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором
каждая строка будет содержать данные о фирме: название, форма собственности,
выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не
включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
from functools import reduce
from json import dump

with open('task_7.txt', 'r', encoding='utf-8') as my_file:
    _firms = [line.split() for line in my_file.readlines()]

names = [n for n, *args_1 in _firms]
profits = [(int(e) - int(c)) for *args_2, e, c in _firms]

pos_els = [el for el in profits if el > 0]
av_profit = reduce(lambda a, b: a + b, pos_els) / len(pos_els)

firms = dict(zip(names, profits))

with open('task_7.json', 'w', encoding='utf-8') as json_file:
    dump([firms, {'average_profit': av_profit}], json_file, ensure_ascii=False,
         indent=2)

"""
4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию. Элементы
выведите в порядке их следования в исходном списке. Для выполнения задания
обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

finished_list = [i for i in original_list if original_list.count(i) < 2]

print(f'Дано:      {original_list}')
print(f'Результат: {finished_list}')

"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

with open('task_2.txt', 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    print(f'Кол-во строк в файле = {len(lines)}')
    [print(f'Кол-во слов в строке_{idx} = {len(line.split())}') for idx, line
     in enumerate(lines, 1)]

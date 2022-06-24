"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово
длинное, выводить только первые 10 букв в слове.
"""
my_string = input("Введите предложение ")
my_word = []
num = 1
for el in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word[el]}")
        num += 1
    else:
        print(f" {num} {my_word[el][0:10]}")
        num += 1

"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""


class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __add__(self, other):
        return Matrix(list(map(str,
                               [self.my_matrix[i][j] + other.my_matrix[i][j]
                                for i in range(len(self.my_matrix)) for j
                                in range(len(self.my_matrix[i]))])))

    def __str__(self):
        if len(self.my_matrix[0]) > 1:
            return ' '.join(list(map(str, [self.my_matrix[i][j] for i in
                                           range(len(self.my_matrix)) for j in
                                           range(len(self.my_matrix[i]))])))
        else:
            return ' '.join(list(map(str, [self.my_matrix[i] for i in
                                           range(len(self.my_matrix))])))


a_1 = Matrix([[4, 1], [3, 7], [8, 9]])
a_2 = Matrix([[5, 7], [10, 6], [1, 4]])
print(a_1)
print(a_2)
print(a_1 + a_2)

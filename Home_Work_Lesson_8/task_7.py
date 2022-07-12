"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число». Реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
класса (комплексные числа), выполните сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""


class Complexnum:
    def __init__(self, a, b):
        self.a = [int(a), int(b)]

    def __add__(self, other):
        ''' Сложение A+B=(a+bi)+(c+di)=(a+c)+(b+d)i '''
        c = [x + y for x, y in zip(self.a, other.a)]
        if c[1] < 0:
            return f'{c[0]}{c[1]}j'
        else:
            return f'{c[0]}+{c[1]}j'

    def __mul__(self, other):
        ''' Умножение (a+bi)⋅(c+di)=(ac−bd)+(bc+ad)i  '''
        d = list(zip(self.a, other.a))  # a, c, b, d
        m, k = d[0][0] * d[0][1] - d[1][0] * d[1][1], d[0][1] * d[1][0] + d[0][
            0] * d[1][1]
        if k < 0:
            return f'{m}{k}j'
        else:
            return f'{m}+{k}j'


a = Complexnum(-5, -6)
b = Complexnum(4, -2)
print(a + b)
print(a * b)

x = complex(-5, -6)
y = complex(4, -2)

print(x + y)
print(x * y)

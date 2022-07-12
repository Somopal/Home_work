"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, data_string):
        self.data_string = data_string

    @classmethod
    def data_format(cls, data):
        try:
            cls.my_data = list(map(int, data.split('-')))
            print(cls.my_data)
        except ValueError:
            print("В дате должны быть только цифры")

    @staticmethod
    def data_validation(string):
        try:
            my_date = list(map(int, Data(string).data_string.split('-')))
            print(string) if (
                    my_date[0] <= 31 and my_date[1] <= 12) else print(
                "Date is invalid")
        except ValueError:
            print("В дате должны быть только цифры")


a = Data("12-01-2020")
Data.data_format("22-03-2022")
a.data_format("23-04-2022")
a.data_validation("64-06-2022")

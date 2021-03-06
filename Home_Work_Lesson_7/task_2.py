"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост
(для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для
пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на
реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def textile(self):
        pass


class Сoat(Clothes):
    @property
    def textile(self):
        print(f"Расход ткани на пальто {round(self.size / 6.5 + 0.5, 2)}")


class Suit(Clothes):
    @property
    def textile(self):
        print(f"Расход ткани на костюм {round(2 * self.size + 0.3, 2)}")


mc = Сoat(10)
mc.textile

mc = Suit(5)
mc.textile

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, m_name):
        self.name = m_name

    @abstractmethod
    def size_coat(self):
        """возвращает размер пальто"""
    @abstractmethod
    def size_suit(self):
        """возвращает размер костюма"""

    @classmethod
    def expense(cls):
        return sum(cls.size_coat()) + sum(cls.size_suit())


class Coat(Clothes):
    def __init__(self,size):
        super(Coat, self).__init__(self.name)
        self.m_size = size

    def size_coat(self):
        return (self.m_size/6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, size):
        super().__init__(self.name)
        self.m_size = size

    def size_suit(self):
        return (2 * self.m_size + 0.3)

my_suit = Suit('summer_style')


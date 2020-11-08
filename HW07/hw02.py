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
    @property
    @abstractmethod
    def size(self) -> float:
        pass
        """возвращает расход ткани"""

class Coat(Clothes):
    def __init__(self, name, size):
        super(Coat, self).__init__(name)
        self.__m_size = size

    @property
    def size(self) -> float:
        return self.__m_size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, size: float):
        super().__init__(name)
        self.__m_size = size

    @property
    def size(self) -> float:
        return 2 * self.__m_size + 0.3

my_suit = Suit("summer", 28)
print(f'Необходимо ткани на костюм {my_suit.name}: {my_suit.size}')

my_coat = Coat("fall", 1.80)
print(f'Необходимо ткани на пальто {my_coat.name}: {my_coat.size}')

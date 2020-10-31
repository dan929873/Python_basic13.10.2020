# абстракция - это обобщенное представление без детального погружения
# можно описать что делает, что имеет этот подвид

# процедурное, функциональное, деклоративное(пишим деклорации) - помимо ООП

import datetime as dt

class Robot:
    def __init__(self, os):
        self.os = os

class Car:
    # атрибуты, к ним можно обратится из любой области
    # engine =""
    # brand = ''
    # create_age = '' -- это можно не создовать
    _collection = []    #_ нижнее подчеркивание это protected можно и прочтать и даже записать но это оч плохо максимум прочитать
    __secret = 'hello secret'   #__ - privat не прочитать за границами класа, но ford_t._Car.__secret - так можно
    def __init__(self, engine, brand, create_age):
        """тут надо описать что эта функция делает"""
        self.engine = engine
        self.brand = brand
        self.create_age = create_age
        self._collection.append(self)

    def run (self):
        print(f'start {self.engine} engine')
        for _ in range(3)
            print('Дыр')

class FordPickUp(Car):
    def __init__(self, name, carrying):
        self.name = name
        self.carryng = carrying
        super().__init__(6.3, 'FORD', dt.datetime.now().year)   #super - возвращает конструктор первого класса, указанного в наследовании

    def hong(self):
        print('aaaaaaa')    #переопределение метода - полиморфизм
        super().hong()

class Transformer (FordPickUp, Robot):
    def __init__(self, name):
        super().__init__(name, 10000)
        Robot.__init__(self, 'SparkOS')

ford_t = Car(1.8, 'Ford', 1932)
chevrolet = Car(6, 'chevrolet', 1987)

p_ford = FordPickUp('Rapter', 2000)



# инкапсуляция ин капсула - закрытая релизация или методы
# черчение диаграм, профайлинг?
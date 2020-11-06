# Перегрузка операторов
# medgiki - методы которые реализуют логические и арифметические операторы

class GarageIter:
    def __init__(self, box):
        self.idx = 0
        self.__box = box
    def __next__(self):
        self.idx += 1
        lenBox = len(self.__box)
        while self.idx-1 < lenBox:

            car = self.__box[self.idx-1]
            if car.vin[-1] == 'q':
                self.idx += 1
            else:
                return car
        raise StopIteration


class Garage:
    def __init__(self, name):
        self.__box = []
        self.name = name

    def add_cars(self, *cars):
        self.__box.extend(*cars)
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__box[item]
        if isinstance(item, str):
            for itm in self.__box:
                if item == itm.name:
                    return itm
            raise KeyError('Error in garage not it car')
    def __iter__(self):
        return GarageIter(self.__iter__())


class Car:
    __vin_codes = {}

    def __init__(self, name, vin):
        self.name = name
        self.vin = vin
    def __str__(self):
        return f'{self.name}: {self.vin}'
    def __eq__(self, other):
        return self.name == other.name
    def __next__(cls, name, vin):
        instance = cls.__vin_codes.get(vin)
        if instance:
            return cls.__vin_codes.get(vin)
        instance = super().__new__(cls)
        cls.__vin_codes[vin] = instance
        return instance

if __name__ == '__main__':
    garage = Garage('Crazy')
    car1 = Car('Ford', 989087879978)
    car2 = Car('Tesla', 34243423243)
    car3 = Car('Lada', 986453286893)

    garage.add_cars(car1, car2, car3)


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        """входные данные:
        speed, color, name, is_police
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} Поехала')

    def stop(self):
        print(f'{self.name} Остановилась')

    def turn(self, direction):
        if direction == "left" or direction == "right":
            print(f'{self.name} повернул на {direction}')
        else:
            print("Это не направление поворода")

    def show_speed(self):
        print(f'{self.name} едет со скоростью: {self.speed}')

class TownCar(Car):
    # 60(TownCar)
    def show_speed(self):
        if self.speed > 60:
            print("Превышение максимальной скорости 60")
        else:
            print(f'{self.name} скороть: {self.speed}')


class SportCar(Car):
    def super_speed(self):
        print(f'{self.name} - спорткар, а это значит по грибы не поедет')

class WorkCar(Car):
    # 40(WorkCar)
    def show_speed(self):
        if self.speed > 40:
            print("Превышение максимальной скорости 40")
        else:
            print(f'{self.name} скороть: {self.speed}')
class PoliceCar(Car):
    def is_polic(self):
        if self.is_police:
            print(f'{self.name} - полицейская машина')
        else:
            print(f'{self.name} - не полицейская машина')

my_police = PoliceCar(110, "Белая", "lada2110", True)
my_police.go()
print(my_police.color)
my_police.is_polic()

my_sportcar = SportCar(300, 'Черная', 'Ferrari', False)
my_sportcar.go()
print(my_sportcar.color)
my_sportcar.show_speed()
my_sportcar.super_speed()

my_city_car = TownCar(45, 'Синяя', 'Ford', False)
my_city_car.go()
print(my_city_car.color)
my_city_car.show_speed()
my_city_car.turn("left")

my_work_car = WorkCar(45, 'Желтая', 'Toyota', False)
my_work_car.go()
print(my_work_car.color)
my_work_car.show_speed()
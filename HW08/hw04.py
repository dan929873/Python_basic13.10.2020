# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import abstractmethod

class Equipment:

    def __init__(self):
        self.warehouse = []


    @abstractmethod
    def speed_work(self) -> float:
        pass

    def distribution(self):
        try:
            firm = input("Введите название подразделения: ")
            type_eq = input("Введите название техники (Printer, Scanner, Xerox)\nв соответсвие с этими названиями: ")
            number_eq = int(input("Введите количество (целое число): "))
            place = {"Подразделение ": firm, "Тип техники": type_eq, "Количество": number_eq}
            self.warehouse.append(place)
        except ValueError:
            print("Введено не целое число")


    def my_print(self):
        for key in self.warehouse:
            print (key)

class Printer(Equipment):
    def __init__(self, id: str, price: float, print_speed: float):
        super(Printer, self).__init__()
        self.__id = id
        self.__price = price
        self.__print_speed = print_speed


    @property
    def speed_work(self) -> float:
        """"return speed"""
        return self.__print_speed

    @property
    def get_data_print(self):
        """"return id price"""
        return self.__id, self.__price


class Scanner(Equipment):
    def __init__(self, id: str, price: float, scanner_speed: float):
        super(Scanner, self).__init__()
        self.__id = id
        self.__price = price
        self.__scanner_speed = scanner_speed

    @property
    def speed_work(self) -> float:
        """"return speed"""
        return self.__scanner_speed

    @property
    def get_data_print(self):
        """"return id price"""
        return self.__id, self.__price


class Xerox(Equipment):
    def __init__(self, id: str, price: float, xerox_speed: float):
        super(Xerox, self).__init__()
        self.__id = id
        self.__price = price
        self.__xerox_speed = xerox_speed

    @property
    def speed_work(self) -> float:
        """"return speed"""
        return self.__xerox_speed

    @property
    def get_data_print(self):
        """"return id price"""
        return self.__id, self.__price


firm1 = Printer('001uu', 2000, 100)
firm2 = Scanner('002uu', 3000, 50)
firm3 = Xerox('003uu', 1000, 30)

firm1.distribution()
firm2.distribution()
firm3.distribution()

firm1.my_print()
firm2.my_print()
firm3.my_print()







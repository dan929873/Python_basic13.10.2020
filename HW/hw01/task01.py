# -*- coding: utf-8 -*-
# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

name = input("how are you name: ")
age = input("how old are you: ")
year = 2020 - int(age)
print("hello ", name, "\nyou born ", year)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print("\nwrite seconds, \nwe will translate into minutes, hours, seconds")
sec = int(input("enter seconds please: "))
my_hours = sec // 3600
my_minutes = (sec - my_hours * 3600) // 60
my_sec = sec - (my_hours * 3600 + my_minutes * 60)
print("hours: ", my_hours, "\nminutes: ", my_minutes, "\nseconds: ", my_sec)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print("\nplease all number 'n', we will translate into 'n + nn + nnn'")
number = input("enter please n: ")
my_number = int(number) + int(str(number + number)) + int(str(number + number + number))
print(my_number)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print("\nenter a positive integer. we will find the largest digit in the number")
integer = int(input("enter please integer: "))
my_max = -1
while integer > 10:
    remainder = integer % 10
    integer //= 10
    if remainder > my_max:
        my_max = remainder
print(my_max)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print("\nwrite down the values of the firm's revenue and costs. \nWe will determine with what financial result the company is working")
revenue = int(input("write please revenue: "))
costs = int(input("write please costs: "))
income = revenue - costs
if income > 0:
    print("the firm has income: ", income)
    ratio = revenue / income
    print("profit to revenue ratio: ", ratio)
    number_employees = int(input("write please number of employees: "))
    firm_profit_per_employee = income // number_employees
    print("firm profit per employee: ", firm_profit_per_employee)
else:
    print("the firm has no income")


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

distans_a = float(input("\nwrite please your first distance: "))
distans_b = float(input("\nwrite please the desired distance: "))
day_distans_b = 1
while distans_a < distans_b:
    distans_a += distans_a/100*10
    day_distans_b += 1
print("day desired distance: ", day_distans_b)
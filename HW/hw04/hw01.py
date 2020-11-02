# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name, output, rate, bonus = argv
try:
    salary = float(output) * float(rate) + float(bonus)
    print(f'{script_name}\nЗарплата: {salary}')
except ValueError:
    print("Введены некоректные данные")



from sys import argv
_, output, rate, bonus, *_ = argv
try:
    salary = float(output) * float(rate) + float(bonus)
    print(f'{script_name}\nЗарплата: {salary}')
except ValueError:
    print("Введены некоректные данные")

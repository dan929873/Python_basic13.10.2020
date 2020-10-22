"""
map
zip
reduce
sorted
max
min
sum
range
round
divmod
"""

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dif(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return ("Деление на ноль")

while True:
    my_quit = input("Для выхода введите q, для продолжения нажмите Enter: ")
    if my_quit == "q":
        break
    elif not my_quit == "":
        print("Можно просто нажать Enter")

    try:
        num01 = float(input("Введите кратное: "))
        num02 = float(input("Введите делитель: "))
        print(dif(num01, num02))
    except ValueError:
        print("Введите число: ")




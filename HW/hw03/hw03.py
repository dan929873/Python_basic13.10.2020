# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_max(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
    return max

def my_min(*args):
    min = max(args)
    for i in args:
        if i < min:
            min = i
    return min

def my_func(*args):
    mmax = my_max(*args)
    mmin = my_min(*args)
    for arg in args:
        if arg < mmax and arg > mmin:
            return mmax + arg

print(my_func(7,2,3))
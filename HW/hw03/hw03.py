# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_max(*args):
    mmax = 0
    for arg in args:
        if arg > mmax:
            mmax = arg
    return mmax

def my_min(*args):
    mmin = my_max(*args)
    for arg in args:
        if arg < mmin:
            mmin = arg
    return mmin

def my_func(*args):
    mmax = my_max(*args)
    mmin = my_min(*args)
    for arg in args:
        if arg > mmin and arg < mmax:
            return mmax + arg

print (my_func(1,33,55))


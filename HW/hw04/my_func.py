def my_enumerate (list, num = 0):
    for srg in list:
        yield num, srg
        num += 1

def my_range(stop, start = 0 , step = 1):
    if stop != 0 and start != 0:
        start, stop = stop, start
    while start < stop:
        yield start
        start += step
my_list = list()

def my_reduce(func, my_list):
    if len(my_list) == 2:
        return func(my_list[0], my_list[1])
    else:
        my_list[0] = my_list[0] * my_list[1]
        my_list.pop(1)
        return my_reduce(func, my_list)

def my_count(firstval=0, end = 10, step=1):
    x = firstval
    while x < end:
        yield x
        x += step

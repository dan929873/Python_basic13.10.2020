from time import (
    sleep,
    time,
    timezone,
)

def my_enumerate(iter_object, start=0):
    for itm in iter_object:
        yield start, itm
        start += 1


def my_cicle(iter_object):
    idx = 0
    while True:
        try:
            sleep(2)
            yield iter_object[idx]
            idx += 1
        except IndexError:
            idx = 0


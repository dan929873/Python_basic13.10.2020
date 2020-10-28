# дзен python https://tyapk.ru/blog/post/the-zen-of-python
# pep
# patterswitchen - переключение языка по горячей клавише
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior - данные про datetime


from lesson.lesson04 import my_modul
import math
import time
import datetime as dt
from itertools import cycle     #много интересного в этой библиотеке
from collections import defaultdict


# enumerate
from lesson.lesson04.my_modul import my_enumerate

mlist = ['a', 'b', 'c', 'd']

# for idx, value in enumerate(mlist, 1):
#     print(idx, value)

#
for idx, value in my_enumerate(mlist, 1):
    print(idx, value)


# print(time.__doc__)

a = '2020-13-05 15:45'

d = dt.datetime.strftime(a, '%Y-%d-%m %H:%M')
d + dt.timedelta(seconds=15765)

print(d)

# for itm in itr_obj:
#     pre_result[''.join(sorted(itm))].append(itm)

# генератор списков list complecented - почитать разницу
a = [3,4,5,3,78,8,34,6]
res = [itm for itm in a if not itm & 1]

# res = {idx : itm for itm in a if not itm & 1}

# @log декораторы

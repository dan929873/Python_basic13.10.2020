# HW
# enum - ?
# zip - ?
# Любую встроенную функцию надо написат
# map zip reduce sorted max min sun range round divmod


# Lesson
# import

def some_f():
    a = 1+2
    return a    #если не указывать return возвращается none

b = some_f()
print(b)

def my_map(funk, iter_obj):

    for itm in iter_obj:
        yield funk(itm)

list = [1,2,3,4]
# list.__iter__

# lambda x: x**3 - x принимает, после : возвращение результата
some_list = [1,2]

try:
    some_list[2]
except IndexError:
    print("зашли за размер")
    pass
finally:
    print("Финал")  # всегда срабатывает


# while True:
#     pass
# else:
#     pass

def some_zip(*args):    #args - кортеж
    """эта функция что то делает - это ее описание
    :param args: параметр для ....
    """
    print(args)

# именовая и позиционная передача ? * **



# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = list()
while True:
    my_list.append(input("write you element: "))
    if input("if you finished, write 'q' ") == 'q':
        break

j = 0
for i in range(int(len(my_list)/2)):
    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    j += 2

print(my_list)

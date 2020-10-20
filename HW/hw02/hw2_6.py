# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
#
# }

my_list = list()
n = 1
while True:
    if not input("Введите q для выхода: ") == "q":
        name = input("название: ")
        price = input("цена: ")
        quantity = input("количество: ")
        unit = input("единица измерения: ")
        my_dict = dict( key_1=name, key_2=price,key_3=quantity,key_4=unit)  # словарь, tuple - кортеж
        my_tuple = (n, my_dict)
        n += 1
        my_list.append(my_tuple)
    else:
        break
    # my_dict.update({key: data})
analitics1 = list()
analitics2 = list()
analitics3 = list()
analitics4 = list()

for list in my_list:
    analitics1.append(list[1].get("key_1"))
    analitics2.append(list[1].get("key_2"))
    analitics3.append(list[1].get("key_3"))
    analitics4.append(list[1].get("key_4"))
print("название:", analitics1)
print("цена:", analitics2)
print("количество:", analitics3)
print("единица измерения:", analitics4)










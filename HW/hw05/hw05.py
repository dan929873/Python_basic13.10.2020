# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

if __name__ == '__main__':

    def summa(name_f):
        try:
            with open(name_f, "r", encoding='UTF-8') as my_r:
                num = my_r.readlines()
                summ = 0
                for n in num:
                    data = n.split(' ')
                for n in data:
                    summ += float(n)
                return summ

        except ValueError:
            pass

    my_num = ["22 77 8 9 90 334 43"]
    try:
        with open("hw05_number.txt", "w", encoding='UTF-8') as my_w:
            my_w.writelines(my_num)
        print(summa("hw05_number.txt"))
    except IOError:
        print("Произошла ошибка ввода-вывода")

#for key, value in db_dict.items():
#   result [key] = sum([int(itm.split{'(')[0]) for itm in value if itm.split('(')[0].isdigit()])
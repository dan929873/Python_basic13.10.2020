# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
if __name__ == "__main__":
    print("Введите текст построчно он сохранится в файл text.txt, для окончания введите пустую строку")
    try:
        with open("text.txt", "w", encoding='UTF=8') as f_obj:
            my_line = input("Введите строку: ")
            while my_line != '':
                f_obj.write(my_line + '\n')
                my_line = input("Введите строку: ")
    except IOError:
        print("Произошла ошибка ввода-вывода!")






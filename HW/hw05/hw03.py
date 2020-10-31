# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


if __name__ == '__main__':
    try:
        num_line = 0

        with open("hw03_name.txt", "r", encoding='UTF-8') as my_f:
            content = my_f.readlines()
            for person in content:
                data = person.split(' ')
                if int(data[3]) < 20000:
                    print(data[0])
    except IOError:
        print("Произошла ошибка ввода-вывода")
    except ValueError:
        print("Некорректного значения, возможно пропущено ФИО")


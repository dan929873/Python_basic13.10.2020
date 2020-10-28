# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


if __name__ == '__main__':
    try:
        num_line = 0

        with open("text.txt", "r", encoding='UTF-8') as my_f:
            for line in my_f:
                num_line += 1
                num_letter = 0
                print(f"{num_line} Строка")
                for letter in line:
                    num_letter += 1
                print(f"Количество букв : {num_letter}")
    except IOError:
        print("Произошла ошибка ввода-вывода")

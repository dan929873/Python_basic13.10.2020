# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
if __name__ == '__main__':
    numbersRU = ['Один', 'Два', 'Три', 'Четыре']
    numbersUS = ['One', 'Two', 'Three', 'Four']
    try:
        with open("hw04_number.txt", "r", encoding='UTF-8') as my_r:
            with open("hw04_number_translate.txt", "w", encoding='UTF-8') as my_w:
                n = 0
                for line in my_r.readlines():
                    if line.startswith(numbersUS[n]):
                        my_w.write(f'{numbersRU[n]} — {n+1}\n')
                    n += 1
    except IOError:
        print("Произошла ошибка ввода-вывода")



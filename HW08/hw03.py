# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class OnlyNum(Exception):
    def __init__(self, text):
        self.text = text

result = []
while True:

    try:
        in_data = input('Введите числа , для выхода знак "q": ')
        if in_data == 'q':
            break
        result.append(float(in_data))
    except ValueError:
        print(OnlyNum('Это не число, не добавлено в список'))

print(result)
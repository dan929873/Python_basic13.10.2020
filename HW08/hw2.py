# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Div_zero(Exception):
    def __init__(self, text):
        self.text = text

a = 3
b = 0

try:
    if b == 0:
        raise Div_zero("Делитель равен нулю")
except Div_zero as dr:
    print(dr)
else:
    print(a/b)

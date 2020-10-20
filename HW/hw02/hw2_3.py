# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
year = (1,2,3,4,5,6,7,8,9,10,11,12)
winter = (1,2,12)
spring = (3,4,5)
summer = (6,7,8)
fall = (9,10,11)
while True:
    number = int(input("write number from 1 to 12: "))
    if not number in year:
        print("no number")
        break
    if number in winter:
        print("winter")
    if number in spring:
        print("spring")
    if number in summer:
        print("summer")
    if number in fall:
        print("fall")

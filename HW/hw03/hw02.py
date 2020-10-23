# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def this_str (str):
    if "0" in str or "1" in str or "2" in str or "3" in str or "4" in str or "5" in str or "6" in str or "7" in str or "8" in str or "9" in str:
        raise ValueError



def one_line(**kwargs):
    return kwargs


while True:
    my_quit = input("Для выхода введите q, для продолжения нажмите Enter: ")
    if my_quit == "q":
        break
    elif not my_quit == "":
        print("Можно просто нажать Enter")

    try:
        name = input("Введите имя: ")
        this_str(name)
        secondname = input("Введите фамилию: ")
        this_str(secondname)
        year_born = int(input("Введите год рождения, формата '2020': "))
        city = input("Введите город проживания: ")
        this_str(city)
        email = str(input("Введите email: "))
        correct = len(email) >= 6 and "@" in email and "." in email
        if not correct:
            print("Неккоректно введен email")
            raise ValueError

        num_phone = int(input("Введите телефон без пробелов и знаков: "))
        print(one_line(your_name = name, your_secondname = secondname, your_year_born = year_born, your_city_life = city, your_email = email, your_num_phone = num_phone))
    except ValueError:
        print("Неккоректно введены данные")


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def show_userdata(name='', surname='', dob='', city='', email='', phone=''):

    print(
        f'Данные пользователя: имя: {name}; \
        фамилия: {surname}; \
        дата рождения: {dob}; \
        город проживания: {city}; \
        e-mail: {email}; \
        телефон: {phone}.')


user_data = input(
    'Введите следующие данные пользователя через запятую: имя, фамилия, дата рождения, город проживания, email, телефон: ')

user_data = list(map(lambda x: x.strip(), user_data.split(',')))

if len(user_data) != 6:
    print('Неверный ввод')

else:
    show_userdata(name=user_data[0], surname=user_data[1], dob=user_data[2],
                  city=user_data[3], email=user_data[4], phone=user_data[5])

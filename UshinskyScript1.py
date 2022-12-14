#!/usr/bin/python3
def func(password):
    x = True
    numbers = 0  # счётчик цифр в пароле
    for i in password:
        if i.isdigit():
            """если находит цифру в пароле счётчик растёт на 1"""
            numbers += 1
    password = password.lower() #переводим значение строки password в нижний регистр
    result = password.find(f'password') #ищем вхождение password

    try: #проверяем условия
        if len(password) < 6:
            x = False
            raise ValueError(f'Недостаточная длина пароля')
        if numbers == len(password):
            x = False
            raise ValueError(f'Ваш пароль состоит из цифр')
        if numbers < 1:
            x = False
            raise ValueError(f'В пароле должна быть хотя бы одна цифра')
        if result>-1:
            x = False
            raise ValueError(f'Пароль не может содержать слово "password" в любом регистре')

    except ValueError as message:
        print(f'{message}')
    return x

print(f'{func(input())}')

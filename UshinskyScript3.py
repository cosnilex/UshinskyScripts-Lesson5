#!/usr/bin/python3
def fibonacci(n):
    if (n <= 1): #первые два числа Фибоначчи 0 и 1
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2)) #Каждое следующее число равно сумме двух предыдущих
try:
    n = int(f'{input("Введите число: ")}')
except ValueError:
    print(f'Вы ввели не число')
try:
    print(f'Ваше число Фибоначчи: {fibonacci(n)}')
except NameError:
    print(f'Неправильный ввод, либо на ввод ничего не поступило')

a = int(input('Введите целое положительное число из нескольких цифр: '))
number_max = 0
while a > 0:
    b = a % 10
    if b > number_max:
        number_max = b
    a = a // 10
print(f'Наибольшая цифра в числе: {number_max}')



















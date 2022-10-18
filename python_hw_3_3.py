a = int(input('Введите число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
def my_func(a, b, c):
    print(f'Cумма двух наибольших чисел: {a + b + c - min(a, b, c)}')
my_func(a, b, c)
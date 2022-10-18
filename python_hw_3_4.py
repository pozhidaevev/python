x = int(input('Введите положительное число "x": '))
y = abs(int(input('Введите отрицательное число "y": ')))
def my_func(x, y):
    print(f'Число "х" в степени "у" равно: {1 / (x ** y)}')
my_func(x, y)
def my_func_1(x, y):
    i = 1
    result = 1
    while i <= y:
        result *= 1 / x
        i += 1
    print(f'Решение другим способом: {result}')
my_func_1(x, y)
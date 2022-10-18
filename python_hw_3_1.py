a = int(input('Введите числитель: '))
b = int(input('Введите знаменатель: '))
if b == 0:
    print('На ноль делить нельзя!')
    b = int(input('Попробуйте еще раз: '))
# Первый вариант
def division_1(a, b):
    print(f'Результат деления: {a / b}')
division_1(a, b)
# Второй вариант
division_2 = lambda a, b: a / b
print(f'Ответ: {division_2(a, b)}')
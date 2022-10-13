your_list = int(input('Создайте список из произвольных чисел. Введите количество чисел в списке: '))
count = []
for i in range(0, your_list):
    number = input('Введите число: ')
    count.append(number)
print(f'Ваш список: {count}')
for i in range(0, len(count)-1, 2):
    count[i], count[i+1] = count[i+1], count[i]
print(f'Решение: {count}')
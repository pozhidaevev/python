def print_sum():
    sum_num = 0
    while True:
        numbers = input('Считаем сумму. Введите числа через пробел, для выхода из программы нажмите "q": ').split()
        for i in numbers:
            if i.lower() == 'q':
                return sum_num
            else:
                sum_num += int(i)
        print(sum_num)
print(print_sum())
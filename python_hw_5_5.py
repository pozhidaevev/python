my_f = open("task_5_5.txt", "w", encoding=("utf-8"))
numbers = '4 5 6 7 8 9 12 3 45 2 5'
my_f.write(numbers)
print(f'Сумма чисел в файле: {sum(map(int, list(numbers.split())))}')
my_f.close()
my_f = open("task_5_2.txt", "r", encoding=("utf-8"))
my_list = [i.strip() for i in my_f]
print(f'Количество строк в файле: {len(my_list)}')
for i in my_list:
    print(f'Количество слов в строке: {len(i.split())}')
my_f.close()
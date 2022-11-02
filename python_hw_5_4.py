with open("task_5_4.txt", "r", encoding=("utf-8")) as my_f:
    my_dict_1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    rus = list(my_dict_1.values())
    my_list = [i for i in my_f]
    my_f.seek(0)
    my_f_new = []
    position = 0
    for i in my_list:
        b = i.replace(my_list[position], rus[position]) + ' ' + i.split()[1] + ' ' + i.split()[2] + '\n'
        position += 1
        my_f_new.append(b)
    print(my_f_new)
with open('task_5_4_new.txt', 'w', encoding='utf-8') as my_f_2:
    my_f_2.writelines(my_f_new)
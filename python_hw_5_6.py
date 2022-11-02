with open('task_5_6.txt', 'r', encoding='utf-8') as my_f:
    list_class = [i.split(':')[0] for i in my_f]
    my_f.seek(0)
    list_hours = [i.split(':')[1:] for i in my_f]
    list_hours_1 = []
    for i in list_hours:
        a = str(i)
        s = [int(i) for i in a.replace('(', ' ').split() if i.isdigit()]
        list_hours_1.append(s)
    list_hours_sum = []
    for i in list_hours_1:
        i = sum(i)
        list_hours_sum.append(i)
    my_dict = dict(zip(list_class, list_hours_sum))
    print(f'Результат: {my_dict}')
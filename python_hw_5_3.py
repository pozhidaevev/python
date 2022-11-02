my_f = open("task_5_3.txt", "r", encoding=("utf-8"))
my_list = [i.strip() for i in my_f]
new_list =[]
new_list_sum = []
for i in my_list:
    if float(i.split()[1]) < 20000.00:
        new_list.append(i)
    new_list_sum.append(i.split()[1])
print(f'Перечисленные ниже сотрудники имеют оклад ниже 20000:')
for i in new_list:
    print(i.split()[0])
def mid_salary():
    for i in my_list:
        return sum(map(float, new_list_sum)) / len(my_list)
print(f'Средний доход на человека: {mid_salary():.2f}')
my_f.close()
import json
my_f_7 = open('task_5_7.txt', 'r+', encoding='utf-8')
print(my_f_7.read())
my_f_7.seek(0)
list_name = [i.split()[0] for i in my_f_7]
my_f_7.seek(0)
list_count = [i.split()[2:4] for i in my_f_7]
list_profit = []
for i in list_count:
    i = int(i[0]) - int(i[1])
    list_profit.append(i)
d_1 = dict(zip(list_name, list_profit))
list_profit_pl = [i for i in list_profit if i > 0]
mid_profit = sum(list_profit_pl) / len(list_profit_pl)
d_2 = {'average_profit': mid_profit}
my_list = [d_1, d_2]
print(my_list)
my_f_7.close()
with open('task_5_7.json', 'w', encoding='utf-8') as t_5:
    json.dump(my_list, t_5)
number_month = int(input('Введите месяц в виде числа от 1 до 12: '))
list_1 = [1, 2, 12]
list_2 = [3, 4, 5]
list_3 = [6, 7, 8]
list_4 = [9, 10, 11]
if number_month  in list_1:
    print('Зима')
if number_month  in list_2:
    print('Весна')
if number_month  in list_3:
    print('Лето')
if number_month  in list_4:
    print('Осень')

seasons = {
    1: 'Зима(Январь)',
    2: 'Зима(Февраль)',
    3: 'Весна(Март)',
    4: 'Весна(Апрель)',
    5: 'Весна(Май)',
    6: 'Лето(Июнь)',
    7: 'Лето(Июль)',
    8: 'Лето(Август)',
    9: 'Осень(Сентябрь)',
    10: 'Осень(Октябрь)',
    11: 'Осень(Ноябрь)',
    12: 'Зима(Декабрь)'
    }
print(seasons[number_month])
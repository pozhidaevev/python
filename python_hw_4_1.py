from sys import argv
def pay():
    try:
        name, hours, rate, bonus = argv
        print(float(hours) * float(rate) + float(bonus))
    except ValueError:
        print('Введите ТРИ значения через пробел (В ТЕРМИНАЛЕ!!! ПРДВАРИТЕЛЬНО УКАЖИТЕ АДРЕС: python .\python_hw_4_1.py ): ')
pay()
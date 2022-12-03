class DataType(Exception):
   def __init__(self, txt):
      self.txt = txt


my_list = []
while True:
    try:
        a = input('Введите число: ')
        if a == 'stop':
            break
        elif not a.isdigit():
            raise DataType('Вы ввели не число!')
        my_list.append(int(a))
    except DataType as err:
        print(err)

print(my_list)

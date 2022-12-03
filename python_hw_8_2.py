class DivisionZero(Exception):
   def __init__(self, txt):
      self.txt = txt


num_1 = int(input('Введите числитель: '))
num_2 = int(input('Введите знаменатель: '))

try:
   if num_2 == 0:
      raise DivisionZero('На ноль делить нельзя!')
except DivisionZero as err:
   print(err)
   num_2 = int(input('Введите знаменатель снова: '))
finally:
    print(num_1 / num_2)
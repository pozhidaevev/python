list_test = [134, 15.515, 'hello', False, [1, 2, 'hi'], (3, 4, 'hey'), True, {5, 4, 98, 'User'}, {1: 'school', 2: 'university'}]
i = 0
while True:
   print(type(list_test[i]))
   i += 1
   if i == len(list_test):
       break
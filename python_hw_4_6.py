from itertools import count, cycle
for i in count(3):
    if i > 10:
        break
    else:
        print(i)
n = 0
for el in cycle(['my', 'name', 'is']):
    n += 1
    if n > 6:
        break
    else:
        print(el)
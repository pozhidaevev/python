from functools import reduce
my_list = [i for i in range(100, 1001, 2)]
def my_func(i1, i2):
    return i1 * i2
print(reduce(my_func, my_list))
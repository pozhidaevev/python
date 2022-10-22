from math import factorial
n = int(input('enter n: '))
def fact(n):
    for i in range(1, n + 1):
        yield i
list_factorial = [factorial(n) for n in fact(n)]
print(list_factorial)
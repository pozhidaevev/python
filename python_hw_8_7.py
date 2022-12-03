class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def create_comp_number(self):
        return complex(self.a, self.b)

    def __add__(self, other):
        return f'Результат сложения: ({self.a + other.a}+{self.b + other.b}j)'

    def __mul__(self, other):
        return f'Результат умножения: ({(self.a * other.a) - (self.b * other.b)}+{(self.a * other.b) + (other.a * self.b)}j)'

num_1 = ComplexNumber(3, 8)
num_2 = ComplexNumber(7, 2)
print(num_1.create_comp_number())
print(num_2.create_comp_number())
print(num_1 + num_2)
print(num_1 * num_2)
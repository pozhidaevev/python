class Cell:
    def __init__(self, unit):
        self.unit = unit

    def __add__(self, other):
        return f'Объединение клеток: {self.unit + other.unit} ячеек.'

    def __sub__(self, other):
        sub_cell = self.unit - other.unit
        if sub_cell > 0:
            return f'Разность клеток: {sub_cell} ячеек.'
        else:
            return f'Операция не возможна. Количество ячеек первой клетки должно быть больше, чем во второй!'

    def __mul__(self, other):
        return f'Создание новой клетки (умножением ячеек): {self.unit * other.unit} ячеек.'

    def __truediv__(self, other):
        return f'Создание новой клетки (путем деления): {self.unit // other.unit} ячеек.'

    def make_order(self, number):
        self.number = number
        str_unit = ''
        for i in range(int(self.unit / self.number)):
            str_unit += f'{"*" * self.number}\n'
        str_unit += f'{"*" * (self.unit % self.number)}'
        print(str_unit)

a = Cell(86)
b = Cell(3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
a.make_order(12)